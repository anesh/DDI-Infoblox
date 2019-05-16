import requests
import json
import re
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

user = 'admin'
pwd = 'infoblox'



url = 'https://192.168.137.3/wapi/v2.7/range'


headers = {'content-type': "application/json"}


json_data = { 
     "start_addr": "45.0.41.20",
     "end_addr": "45.0.41.101",
     "server_association_type": "FAILOVER" ,
     "failover_association": "TESTFO" 
}





payload = json.dumps(json_data)
response = requests.post(url, auth=(user, pwd), headers=headers, data=payload,verify=False)
print response.text
