# power digit sum
def powerofn(a,n):  # to find a power n
    if n<1:
        return 1
    return  a*powerofn(a,n-1)
def digitsum(n):    #to sum digits of n
    if n<1:
        return 0
    return int(n%10)+digitsum(int(n/10))
def powerdigitsum (a,n):    # to find a power n and sum digits
    return digitsum(powerofn(a,n))
a=2
n=1000
print (powerdigitsum(a,n))
