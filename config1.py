fin=open("running-config.cfg")
file_read=fin.read()
def list_ifname_ip():
	mydict=dict()
	newdict=dict()	
	for line in file_read.split():
		word=line.strip()
		if word not in mydict:
			mydict[line]=1
		else:
			mydict[line]+=1
#	print(mydict)
	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))	
	print(mylist)

