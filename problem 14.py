#Longest coltaz sequence upto n
def countchain(n):
    if n<=1:
        return 1
    if(n%2==0):
        return 1 + countchain(int(n/2))
    return 1 + countchain(3*n+1)
        
n=1000000 # ANS---837799 chain -- 525
maxchain=0
ans=0
for i in range(n+1,1,-1):
    temp=countchain(i)
    #print (temp,i)
    if(temp>maxchain):
        maxchain=temp
        ans=i
print (ans)