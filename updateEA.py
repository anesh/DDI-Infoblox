import requests
import json
requests.packages.urllib3.disable_warnings() 


f1 = open('att.txt','r')

attributes = f1.read().splitlines() 

citylist=[]

for att in attributes:
     citylist.append({'value': att})


newdict={"list_values": citylist}
url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLlZMQU4:VLAN"
#url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLkNpdHk:City"
#url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLlNpdGUgQ29kZQ:Site%20Code"
#url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLkJ1c2luZXNzIFVuaXQ:Business%20Unit"
#url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLkVudmlyb25tZW50:Environment"
#url = "https://10.2.61.100/wapi/v2.7/extensibleattributedef/b25lLmV4dGVuc2libGVfYXR0cmlidXRlc19kZWYkLkNvdW50cnk:Country"
payload = json.dumps(newdict) 
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, auth=('anesh.ponnarasseryke', '####'), data=payload, headers=headers,verify=False)
print response.text
