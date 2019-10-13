#Numberlettercount
def lettercount(numwords,no,f):     #return letter count of n^th no upto 999
    count=0
    if(no==0):
        return 0
    if(f):                          #for no 1<= n <20
        x=no%100
        no=int(no/100)
        if x<20 :
            count = count + numwords[int(x)] + lettercount(numwords,no,False)
        else:
            count = count + numwords[int(x%10)]
            x=int(x/10)
            count = count + numwords[int(x)*10] + lettercount(numwords,no,False)
    else:                           #for no 20<= n <1000
        x=no%10
        no/=10
        count = count + numwords[int(x)] + lettercount(numwords,no,False)
    return count
def countletterrange(y):            #function to count upto 1000
    count=0
    di={                            #for letter count exp. for 1(one) = 3
        0:0,
        1:3, 
        2:3,
        3:5,
        4:4,
        5:4,
        6:3,
        7:5,
        8:5,
        9:4,
        10:3,
        11:5,
        12:5,
        13:8,
        14:8,
        15:7,
        16:7,
        17:9,
        18:8,
        19:8,
        20:6,
        30:6,
        40:5,
        50:5,
        60:5,
        70:7,
        80:6,
        90:6,
        100:7,
        1000:8
    }
    if y<1:
        return 1        # for 1000
    count+=lettercount(di,y,True)
    return count + countletterrange(y-1)
print (countletterrange(100))