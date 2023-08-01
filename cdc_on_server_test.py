from fpds import fpdsRequest 
import json


request = fpdsRequest(
    LAST_MOD_DATE="[2023-07-01, 2023-07-04]",
    AGENCY_CODE="7523"
)

# Records saved as a python list
records = request()

# writing as JSON
with open(r'C:\Users\johnp\OneDrive - Delphi Consulting Solutions\Delphics\Project Independence\API Downloads\07_31_test.json','w') as file:
    json.dump(records, file)






# Code run python scripts concurrently
# https://stackoverflow.com/questions/28549641/run-multiple-python-scripts-concurrently