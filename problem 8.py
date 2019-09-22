from random import randint
import numpy
def randomnum(x):
    start=10**(x-1);
    end=10**n-1;
    return randint(start,end);

n=1000;
digit=13;
x=str(randomnum(n));
x=[int(i) for i in x];
max=0;
for i in range(n-digit+1):
    temp=numpy.prod(x[i:i+13]);
    if(temp>max):
        max=temp;
print(max);