import requests
import json
requests.packages.urllib3.disable_warnings() 


f1 = open('fqdns.txt','r')

postvalues = f1.readlines() 

for postvalue in postvalues:
	column=postvalue.split()
	fqdn= str(column[0])+".ns.ctc"
	ipaddress = str(column[1])

	url = "https://10.2.61.100/wapi/v2.7/record:host"

	values = { "name":fqdn, "ipv4addrs":[{"ipv4addr":ipaddress}],"view": "Internal" }


	payload = json.dumps(values) 
	headers = {'content-type': "application/json"}
	response = requests.request("POST", url, auth=('anesh.ponnarasseryke', 'Adimurai@777'), data=payload, headers=headers,verify=False)
	print response.text
