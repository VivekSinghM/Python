def countdiv(n):
    c=1;
    for i in range(1,int(n/2+1)):
        if(n%i==0):
            c+=1;
    return c;
div=500;
count=0;
n=0;
i=1;
while count<div :
    n+=i;
    #print(n,countdiv(n));
    count=countdiv(n);
    i+=1;
print(n)