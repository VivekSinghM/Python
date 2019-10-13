#sUM squar difference

n=100
l=[i for i in range(1,n+1)]
sqrsum=sum([i*i for i in l])
sumsqr=sum(l)
sumsqr=sumsqr*sumsqr
print(sumsqr-sqrsum)