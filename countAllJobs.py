import requests
import json
from jsontraverse.parser import JsonTraverseParser
import sys

rota = ""

# headers = {
#    'X-API-KEY': ''
# }

## request API
r = requests.get(url=rota)

## JSON PARSE
data = r.json()
json_string = json.dumps(data)
parser = JsonTraverseParser(json_string)

## Contagent
jobName = parser.traverse("Jobs.JobName",force_list=1)

if jobName != None:
    allJobs = len(jobName)

else:
    allJobs = 0

print(allJobs)