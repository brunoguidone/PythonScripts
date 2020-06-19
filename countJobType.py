import requests
import json
from jsontraverse.parser import JsonTraverseParser
import sys

countJobs = ''

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

## Contagens
jobName = parser.traverse("Jobs.JobName")


#Retrieve variable from SH
#PARM = sys.argv[1]
PARM = "QueueProcessJob"

if jobName != None:
    countJobType = jobName.count(PARM)

else:
    countJobType = 0


print(countJobType)