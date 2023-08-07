from fpds import fpdsRequest
import json  


# https://pypi.org/project/fpds/
# https://stackabuse.com/executing-shell-commands-with-python/
# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

# https://www.guru99.com/python-json.html
# Method	Description
# dumps()	encoding to JSON objects
# dump()	encoded string writing on file
# loads()	Decode the JSON string
# load()	Decode while JSON file read







request = fpdsRequest(
    LAST_MOD_DATE="[2022/01/01, 2022/01/02]",
    AGENCY_CODE="7523"
)

# Records saved as a python list
records = request()
# # or equivalently, explicity call the `parse_content` method
# records_parsed = request.parse_content()

# writing as STRING
with open(r'C:\Users\johnp\OneDrive - Delphi Consulting Solutions\Delphics\Project Independence\API Downloads\cli_results.txt','w') as file:
    results_as_dict = json.dumps(records,indent=4)
    file.write(results_as_dict)

# writing as JSON
with open(r'C:\Users\johnp\OneDrive - Delphi Consulting Solutions\Delphics\Project Independence\API Downloads\cli_results.json','w') as file:
    json.dump(records, file)

# Code run python scripts concurrently
# https://stackoverflow.com/questions/28549641/run-multiple-python-scripts-concurrently