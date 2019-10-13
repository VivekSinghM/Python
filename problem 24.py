#lexicographic permutations
def permutation(wordli,start,end):
    permutationli=[]
    if start==end:
        x=["test"]
        x[0]=''.join(wordli)
        return x
    else:
        for i in range(start,end+1):
            wordli[i],wordli[start]=wordli[start],wordli[i]
            permutationli+=permutation(wordli,start+1,end)
            wordli[i],wordli[start]=wordli[start],wordli[i]
    return permutationli
def lexicographicPermut(li,n):
    li=[str(i) for i in li]
    allpermutation=permutation(li,0,len(li)-1)
    allpermutation.sort()
    return allpermutation[n-1]
li=[1,2,3,4,5,6,7,8,9]
n=100000
print(lexicographicPermut(li,n))        #ans=358926471
