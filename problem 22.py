# Name Scores
# x=open("name.txt","w")
# x.close
def countscore(word,alpha):                 #count and return score of word using dict
    if(len(word)<=1):
        return alpha[word[0]]
    return alpha[word[0]]+countscore(word[1:],alpha)
def totalNameScore(li):
    totalScore=0
    nameScore={}                                        # dict to score score of diff words
    alpha={ chr(i):i-64 for i in range (65,91) }        # creat a dict of A-Z with Score 1-26
    print (alpha)
    for i in range(len(li)):
        w=li[i].upper()                 # convert word int uppercase 
        try:                            # check if nameScore(dict) have word or not if not then creat new entery 
            temp = nameScore[w]
        except KeyError:
            temp=countscore(w,alpha)    
            nameScore[w]=temp           # creat new entery
        totalScore += (i+1) * temp      # word score * word position 
    return totalScore

x=open("name.txt")
li=[]
li=[ j for i in x for j in i.split()]
print (li)
li.sort()
print(li)
print (totalNameScore(li))
