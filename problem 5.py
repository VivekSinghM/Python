#Smalest multiple
n=20;
f=True;
c=n;
while (True):
	c+=1;
	for i in range (2,n+1):
		if(c%i!=0):
			f=False;
			break;
	if(f):
		print(c);
		break;
	f=True;