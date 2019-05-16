f = open("att.txt", "w")
for i in range(4094):
	i=i+1
	print i
	f.write(str(i)+"\n")
