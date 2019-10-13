#ambicable number
def divsum(n,m):
    if(m<=1):
        return 1
    if n%m==0:
        return m + divsum(n,m-1)
    else :
        return 0 +   divsum(n,m-1)
def properdivsum (n):
    temp = divsum (n,n/2)
    if n == divsum(temp,temp/2):
        return True
    return False
def countfrom(n):
    if(n==1):
        return 0
    if properdivsum(n):
        return n + countfrom(n-1)
    return 0 + countfrom(n-1)
n=1000
print(countfrom(n))