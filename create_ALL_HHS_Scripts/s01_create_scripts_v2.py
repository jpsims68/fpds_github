import os

base_dir = r'C:\Users\Administrator\Documents\python_scripts'

base_output_dir = os.path.join(base_dir, 'fpds_output_files')
xml_output_dir = os.path.join(base_output_dir, 'xml_output')
json_output_dir = os.path.join(base_output_dir, 'json_output')

# os.mkdir(base_output_dir)
# os.mkdir(xml_output_dir)
# os.mkdir(json_output_dir)

def get_script_template():
    return f'''
{import_statement}

agency_code='{agency_code}'
entry_action_type='Created'
date_extract_from='{date_extract_from}'
date_extract_thru='{date_extract_thru}'

fpds = FPDS(agency_code=agency_code, entry_action_type=entry_action_type, date_extract_from=date_extract_from, date_extract_thru=date_extract_thru)
fpds.process_all_api_urls(r'{base_dir}')
'''


agency_scope = [ '7500', '7501', '7502', '7503', '7504', '7505', '7506', '7507', '7508', '7509',
                 '750S', '7510', '7511', '7512', '7515', '7516', '7520', '7521', '7522', '7523', 
                 '7524', '7525','7526', '7527', '7528', '7529', '7530', '7537', '7540', '7545', 
                 '7550', '7555', '7558', '7559', '7565', '7570', '7571', '7572', '7573', '7574', 
                 '7575', '7576', '7577', '7590', '7593']

periods = [ ('2018-10-01', '2019-09-30'),
            ('2019-10-01', '2020-09-30'),   
            ('2020-10-01', '2021-09-30'),
            ('2021-10-01', '2022-09-30'),   
            ('2022-10-01', '2023-09-30')]

scripts_created = []
script_count = 10

scripts = {}
for cntr, agency in enumerate(agency_scope):
    for period in periods:

        agency_code = agency
        date_extract_from = period[0]
        date_extract_thru = period[1]

        script_number = cntr % script_count

        script_filename = os.path.join(base_dir, "script_" + str(script_number) + ".py")

        if script_filename not in scripts_created:
            import_statement = 'from clsFPDS_v2 import FPDS'
            scripts_created.append(script_filename)
        else:
            import_statement = ''

        script_template = get_script_template()

        with open(script_filename, 'a') as f:
            f.write(script_template)

