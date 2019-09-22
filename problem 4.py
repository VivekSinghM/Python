#Largest palindrom product of n digit
n=3;
s="";
f=False;
for i in range (n):
	s=s+'9';
s=int(s);
for i in range (s+1,1,-1):
	for j in range (s+1-i,2,-1):
		x=str(i*j);
		if(x[:]==x[::-1]):
			print(i,"X",j);
			f=True;
			break;
	if(f):
		break;
input();
