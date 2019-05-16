import requests
import json
requests.packages.urllib3.disable_warnings() 
import re
from bs4 import BeautifulSoup

sep = "/"
user = 'anesh.ponnarasseryke'
pwd = 'Adimurai@999'


req_params = {'view': 'External' }
url = "https://10.2.61.100/wapi/v2.7/record:a?name~=ns1-gslb.marks.com"
response = requests.request("GET", url, params=req_params, auth=(user,pwd),verify=False)
values= response.text
jsonv = json.loads(values)
x = jsonv[0]['_ref']
refid = x.split(sep,1)[1]
print refid

values = { 'use_ttl': True,'ttl': 300 }
payload = json.dumps(values)
url = "https://10.2.61.100/wapi/v2.7/record:a/"+refid
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, auth=(user,pwd), data=payload, headers=headers,verify=False)
print response.text

