#special pythagorean triplet
sum=1000
def triplet(sum):    
    for a in range(1,int(sum/3)+1):
        for b in range(a+1,int(sum/2)+1):
            c=sum-a-b
            if(a*a+b*b==c*c and a+b+c==sum):
                return [a,b,c]
print(triplet(sum))