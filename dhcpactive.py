f1 = open('hoffdhcpactive.txt','r')
f2 = open('netwok2check.txt','r')

qiptable = []
notinsyslog = []
lines= f1.readlines()
networks=f2.readlines()

for line in lines:
	ip= line.split()[0]
	threeoctets=".".join(ip.split('.')[0:-1])
	qiptable.append(threeoctets)

for network in networks:
	notinsyslog.append(network.rstrip('\n'))

#remove duplicates in a list using set function 
a = set(qiptable)
b = set(notinsyslog)
print a & b
 
