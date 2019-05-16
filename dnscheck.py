import dns.resolver
import xlsxwriter

f1 = open('zones.txt','r')


book = xlsxwriter.Workbook('nameserver.xlsx')
sheet = book.add_worksheet("report")




fqdns = f1.read().splitlines() 
print fqdns
intresolver = dns.resolver.Resolver()
intresolver.nameservers = ['10.255.255.253']
intresolver.timeout = 2
intresolver.lifetime = 2

extresolver = dns.resolver.Resolver()
extresolver.nameservers = ['199.202.145.0']
extresolver.timeout = 2
extresolver.lifetime = 2


row=0
col=0

for fqdn in fqdns:
	row=row+1
	col=0
        sheet.write(row, col,fqdn )
	try:
		answers= intresolver.query(fqdn, 'A')
	except:
		print "cannotberesolved: "+fqdn
	try:
                answers= extresolver.query(fqdn, 'A')
        except:
                print "cannotberesolved: "+fqdn


	for answer in answers:
		col=col+1
		print fqdn,answer.to_text()
		sheet.write(row, col,answer.to_text() )



book.close()
