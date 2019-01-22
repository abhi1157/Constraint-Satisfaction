
'''

ABHINAV GUPTA
2015B4A70602P

'''

''' enter 1 to see dfs with BT without heuristic and enter 2 for heuristic if you just want to see the output for n>4 where n is
odd you can see it by entering 2 when asked I have used a standard algo for that which is
'''
import math
import time
from Assign4 import *
from newtest import *
import time

t=int(input("Please enter integer from 1 to 2"))
start = time.clock()
if(t==1):
    n=int(input("Enter size of magic square"))
    #m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[]
    for i in range(n):
        lp=[]
        for j in range(n):
            lp.append(0)
        m.append(lp)
    print('Running DFS with Backtracking')
    DFS(m,n)
    print(m)
    totaltime = time.clock() - start
    print('totaltime for current code',totaltime)
    GUI(n,m)

if(t==2):
    n=int(input("Enter size of magic square"))
    f=1
    if(n>4):
        f=int(input("for n>4 if you want to run DFS method enter 1 else if you just want to see the output press2"))

    if(f==1 or n%2==0):
        dicti={}
        for i in range(1,n*n+1):
            dicti[i]=[]
            for k in range(1,n*n+1):
                dicti[i].append(k)
        Visit=[0]*(n*n)
        m=[]
        for i in range(n):
            lp=[]
            for j in range(n):
                lp.append(0)
            m.append(lp)

        print('Running DFS with Backtracking with MRV')
        x=DFS_BT_MRV(m,n//2,n//2,n,dicti,Visit)
        print(m)
        print('maxDepth',n*n-1)#always dependent on n
        print('total nodes generated with MRV',x)
        totaltime = time.clock() - start
        print('totaltime for current code',totaltime)
        GUI(n,m)

    elif(f==2):
        GUI(n,Square(n))
