from fpds import fpdsRequest
import json


request = fpdsRequest(
    LAST_MOD_DATE="[2023-07-01, 2023-07-04]",
    AGENCY_CODE="7523"
)

# Records saved as a python list
records = request()

# writing as JSON
<<<<<<< HEAD
with open(r'C:\Users\johnp\OneDrive - Delphi Consulting Solutions\Delphics\Project Independence\API Downloads\07_31_test.json','w') as file:
=======
with open(r'C:\Users\Administrator\Documents\api_downloads\cdc_run_from_server_5_yr.json', 'w') as file:
>>>>>>> c3507764cb77fb4c64bbe4c7b7c892a5263f51b3
    json.dump(records, file)





# Code run python scripts concurrently
# https://stackoverflow.com/questions/28549641/run-multiple-python-scripts-concurrently
