import requests
import json
import re
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

user = 'admin'
pwd = 'infoblox'



url = 'https://192.168.137.3/wapi/v2.7/network'


headers = {'content-type': "application/json"}


json_data = { "network": "45.0.44.0/24",
     	      "members": [
               {
                  "_struct": "dhcpmember",
                  "ipv4addr" : "192.168.137.3"

               },
               {
                  "_struct": "dhcpmember",
                  "ipv4addr" : "192.168.137.2"

               }

             ],
             "comment": "testnetwork"
            }





payload = json.dumps(json_data)
response = requests.post(url, auth=(user, pwd), headers=headers, data=payload,verify=False)
print response.text
