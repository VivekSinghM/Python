#Even Febonacci number
n=4000000
a=0;
b=1;
c=a+b;
while c<n :
    print(c);
    a=b;
    b=c;
    c=a+b;
Input();