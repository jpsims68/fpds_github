from bs4 import BeautifulSoup
import requests


class FPDS:

    def __init__(self, agency_code, entry_action_type, date_extract_from, date_extract_thru):
        self.agency_code = agency_code
        self.entry_action_type = entry_action_type
        self.date_extract_from = date_extract_from
        self.date_extract_thru = date_extract_thru

        self.last_api_link = None
        self.all_api_urls = None
        self.last_entry_start_counter = None
        self.initial_search_url = self.get_initial_search_url()

    def get_initial_search_url(self):
        # url_base_prefix = 'https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q='
        # url_base_suffix = '&templateName=1.5.3&indexName=awardfull&x=24&y=11&sortBy=CREATED_DATE&asc=Y'
        # url_parms = 'AGENCY_CODE:' + options['agency_code'] '+CREATED_DATE:[2018/10/01,2023/09/30]'
        if self.entry_action_type == 'Created':
            initial_search_url = f'https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q=AGENCY_CODE:{self.agency_code}+CREATED_DATE:[{self.date_extract_from},{self.date_extract_thru}]&templateName=1.5.3&indexName=awardfull&x=24&y=11&sortBy=CREATED_DATE&asc=Y'
        if self.entry_action_type == 'Modified':
            initial_search_url = f'https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q=AGENCY_CODE:{self.agency_code}+MODIFIED_DATE:[{self.date_extract_from},{self.date_extract_thru}]&templateName=1.5.3&indexName=awardfull&x=24&y=11&sortBy=CREATED_DATE&asc=Y'
        return initial_search_url

        # note: need to eventually add an entry for just PDs

    def get_last_api_link(self):
        if self.last_api_link != None:
            return self.last_api_link
        else:
            source = requests.get(self.initial_search_url)
            soup = BeautifulSoup(source.content, 'lxml')
            links = [link.get('href') for link in soup.find_all('link')]

            # search soup.links.rel tags for last ... if it is not there then last_api_link = NONE
            # (i.e., if initial_search_url page has no 'last' link then last_api_link = NONE)

            if len(links) > 1:
                self.last_api_link = links[1]
            else:
                self.last_api_link = None
            return self.last_api_link

    def get_last_entry_start_counter(self):
        # check to make sure the last api link has been checked for before determining it is None
        if self.last_api_link == None:
            self.last_api_link = self.get_last_api_link()
        # now that it has been checked for and is None we can confidently return None
        if self.last_api_link == None:
            return None
        else:
            start = str(self.last_api_link).index('&start=')
            last_entry_start_counter = self.last_api_link[(start+7):]
            return last_entry_start_counter

    def get_all_api_urls(self):
        if self.all_api_urls == None:
            if self.last_api_link == None:
                self.last_api_link = self.get_last_api_link()
            if self.last_entry_start_counter == None:
                self.last_entry_start_counter = self.get_last_entry_start_counter()
            if self.last_entry_start_counter == None:
                exit
            else:
                cntr = self.last_entry_start_counter
                template = str(self.last_api_link).replace(
                    'start=' + self.last_entry_start_counter, 'start=XXXXX')
                # all_api_urls = [template.replace('start=XXXXX', 'start=' + str(page_start_counter)) for page_start_counter in range(0,int(cntr)+1,10)]
                all_api_urls = [(page_start_counter, template.replace('start=XXXXX', 'start=' + str(
                    page_start_counter))) for page_start_counter in range(0, int(cntr)+1, 10)]
                return all_api_urls

    def process_all_api_urls(self, file_dest_path=''):
        if self.all_api_urls == None:
            self.all_api_urls = self.get_all_api_urls()

        def get_file_name(cntr):
            return str(self.agency_code) + '_' + self.entry_action_type + '_' + str(self.date_extract_from).replace('-', '_') + '_' + ('000000' + str(cntr))[-6:]

        try:
            for api_url in self.all_api_urls:
                cntr = api_url[0]
                url = api_url[1]
                file_name = get_file_name(cntr) + '.xml'
                r = requests.get(url)
                txt = r.text
                with open(file_dest_path + '/' + file_name, 'w') as file:
                    file.write(txt)
                    print(str(cntr) + ' of ' + self.last_entry_start_counter)
        except:
            print(
                f'there was an error processing the api_urls ... moving on to the next search')

        finally:
            pass
