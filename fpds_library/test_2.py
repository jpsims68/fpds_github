from fpds import fpdsRequest
import json


request = fpdsRequest(
    LAST_MOD_DATE="[2023/07/01, 2023/07/04]",
    AGENCY_CODE="7523"
)

# Records saved as a python list
records = request()

with open(r'C:\Users\Administrator\Documents\api_downloads\cdc_test.json', 'w') as file:
    json.dump(records, file)
