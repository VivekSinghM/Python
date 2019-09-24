#largest sum in a gried of n X n
from random import randint
import numpy
def randomupto(x):
    x=(10**x)-1;
    return randint(0,x);

def maxpro(grid,i,j,digit):
    pro1=numpy.prod(grid[i][j+1-digit:j+1]);
    pro2=numpy.prod(grid[i][j:j+digit+1]);
    pro3=numpy.prod([grid[i-p][j] for p in range(digit)]);
    pro4=numpy.prod([grid[i-p][j-p] for p in range(digit)]);
    pro5=numpy.prod([grid[i-p][j+p] for p in range(digit)]);
    pro6=numpy.prod([grid[i+p][j] for p in range(digit)]);
    pro7=numpy.prod([grid[i+p][j-p] for p in range(digit)]);
    pro8=numpy.prod([grid[i+p][j+p] for p in range(digit)]);
    l=[pro1,pro2,pro3,pro4,pro5,pro6,pro7,pro8];
    m=0
    for i in l:
        if(m<i):
            m=i;
    return m;
n=20;
x=2;
digit=4;

grid = [[randomupto(x) for i in range(n)]  for j in range (n)];
#print (grid);
ma=0;
#mlist=[];
for i in range (3,n-3):
    for j in range (3,n-3):
        cpro=maxpro(grid,i,j,digit);
        if(ma<cpro):
            ma=cpro;
            #mlist=cpro[1:];
print (ma);

