from fpds import fpdsRequest
import json


request = fpdsRequest(
    LAST_MOD_DATE="[2018/10/01, 2023/09/30]",
    AGENCY_CODE="7523"
)

# Records saved as a python list
records = request()

# writing as JSON
with open(r'C:\Users\Administrator\Documents\api_downloads\cdc_run_from_server_5_yr.json', 'w') as file:
    json.dump(records, file)


# # writing as STRING
# with open(r'C:\Users\johnp\OneDrive - Delphi Consulting Solutions\Delphics\Project Independence\API Downloads\cli_results.txt','w') as file:
#     results_as_dict = json.dumps(records,indent=4)
#     file.write(results_as_dict)


# Code run python scripts concurrently
# https://stackoverflow.com/questions/28549641/run-multiple-python-scripts-concurrently
