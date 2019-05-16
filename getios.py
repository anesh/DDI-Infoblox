import os
import paramiko
import xlsxwriter
import socket
import re
import sys
import time
from ciscoconfparse import CiscoConfParse
import getpass


username = raw_input('Enter username for device login:')
password =  getpass.getpass()

f1 = open('device.txt','r')

book = xlsxwriter.Workbook('ios.xlsx')
sheet = book.add_worksheet("report")

header_format = book.add_format({'bold':True , 'bg_color':'yellow'})
header = ["DeviceIP","Hostname","OS"]
for col, text in enumerate(header):
	sheet.write(0, col, text, header_format)



devices = f1.readlines()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
config =[]
row=0

for device in devices:
    row=row+1
    column = device.split()
    print column[1]
    sheet.write(row, 0,column[0] )
    sheet.write(row, 1,column[1] )
    try:
	ssh.connect(column[0], username=username, password=password,timeout=5,allow_agent=False,look_for_keys=False)
	stdin,stdout,stderr = ssh.exec_command('show version ')
	version=stdout.read()
	if not re.search('Cisco Nexus Operating System \(NX-OS\) Software', version):
		sheet.write(row,2,"IOS" )
	else:
                sheet.write(row,2,"NX-OS")

    except socket.error, e:
        output = "Socket error"
	sheet.write(row,3,output)
    except paramiko.SSHException:
        output = "Issues with SSH service"
	sheet.write(row,3,output)
    except paramiko.AuthenticationException:
        output = "Authentication Failed"
	sheet.write(row,3,output)
    except: 
        print "error occured"   
	ssh.close()
        continue

    
book.close()    
f1.close()
