

import xml.etree.ElementTree as ET
from fpds import fpdsXML
import json
import os

xml_output_dir = r'C:\Users\Administrator\Documents\api_downloads'
json_output_dir = r'C:\Users\Administrator\Documents\api_downloads\json_conversions'

# get list of xml files so we can convert them to json
for xml_file in os.listdir(xml_output_dir):
    full_xml_file_path = os.path.join(xml_output_dir, xml_file)
    if full_xml_file_path.endswith('.xml'):
        # print(full_xml_file_path)

        tree = ET.parse(full_xml_file_path)
        myXML = fpdsXML(content=tree)

        entries = myXML.jsonified_entries()

        json_full_file_path = os.path.join(
            json_output_dir, xml_file.replace('.xml', '.json'))
        with open(json_full_file_path, 'w') as new_json_file:
            json.dump(entries, new_json_file)
