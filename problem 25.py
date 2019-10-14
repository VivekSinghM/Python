def digitcount(n):
    count = 1
    if n<=1:
        return count
    return count+digitcount(int(n/10))
n = 3
a=0
b=1
c=0
while (digitcount(c)<=n):
    c=a+b
    print(c)
    a,b=b,c
print(c)