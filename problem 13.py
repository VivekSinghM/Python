from random import randint;
def rendomnum(n):
    start=10**(n-1)
    end=(10**n)-1
    return randint(start,end)
digits=50
num=100
printdigit=10
s=str(sum([rendomnum(digits) for i in range(num)]))
for i in range(printdigit):
    print(s[i],end="")