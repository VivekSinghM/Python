# factorial difgit sum
def fact (n):
    if n==1:
        return 1
    return n*fact(n-1)
def digitSum (n):
    if n==0:
        return 0
    return n%10 + digitSum (int(n/10))
n=100
print (digitSum(fact(n)))