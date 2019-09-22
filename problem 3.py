#Largest prime number
import sympy;
n=600851475143;
n2=int(n/2);
f=False;
for i in range (n2,3,-1):
    if(n%i==0):
        if(sympy.isprime(i)):
        	print(i);
        	break;
input();