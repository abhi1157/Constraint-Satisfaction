'''

ABHINAV GUPTA
2015B4A70602P

'''
import math
import turtle
from copy import deepcopy

def AllDiff(mat):
    k=len(mat)
    lis=[]
    for i in range(k):
        for j in range(k):
            if(mat[i][j] in lis):
                return False
            lis.append(mat[i][j])
    return True

def sumConstraint(mat):
    leng=len(mat)
    Number=(leng*(leng*leng+1))/2
    maxi=-1
    #horizontal
    change=-1
    for i in range(len(mat)):
        sum=0
        flag=0
        for j in range(len(mat[0])):
            if(mat[i][j]==0):
               flag=1
            sum+=mat[i][j]
        if(change is -1 and flag is 0):
            change=sum
        if(flag is 1):
            maxi=max(maxi,sum)
        if(flag is 1 and (sum>change and change is not -1)):
            return False
        if((sum!=change or sum < maxi or sum!=Number) and flag is 0):
            return False

    #vertical
    for i in range(len(mat)):
        sum=0
        flag=0
        for j in range(len(mat[0])):
            if(mat[j][i]==0):
               flag=1
            sum+=mat[j][i]
        if(change is -1 and flag is 0):
            change=sum
        if(flag is 1):
            maxi=max(maxi,sum)
        if(flag is 1 and (sum>change and change is not -1)):
            return False
        if(flag is 0 and(sum!=change or sum < maxi or sum!=Number)):
            return False
    #diagonal1
    sum=0
    flag=0
    for i in range(len(mat)):
        if(mat[i][i]==0):
            flag=1
        sum+=mat[i][j]
    if(change is -1 and flag is 0):
        change=sum
    if(flag is 1):
        maxi=max(maxi,sum)
    if(flag is 1 and (sum>change and change is not -1)):
        return False
    if(flag is 0 and (sum!=change or sum < maxi or sum!=Number)):
        return False


    #diagonal2
    sum=0
    flag=0
    leng=len(mat)
    for i in range(len(mat)):
        if(mat[i][leng-i-1]==0):
            flag=1
        sum+=mat[i][leng-i-1]
    if(change is -1 and flag is 0):
        change=sum
    if(flag is 1):
        maxi=max(maxi,sum)
    if(flag is 1 and (sum>change and change is not -1)):
        return False
    if(flag is 0 and (sum!=change or sum < maxi or sum!=Number)):
        return False

    return True

total=0
maxii=0
def DFS(CSP,n):
    Visited=[False]*(n*n)
    print('max depth',DFS_BT(CSP,0,0,Visited,n,0))
    global total
    print('total nodes grnerated without heuristic',total)


def DFS_BT(matrix,i,j,Visited,n,count):
    flag=0
    global total
    global maxii
    if(count>maxii):
        maxii=count
    for k in range(1,n*n+1):

        if(Visited[k-1] is False):
            matrix[i][j]=k
            total=total+1
            Visited[k-1]=True
            if(sumConstraint(matrix)==True):
                if(j is n-1 and i is n-1):

                    return 0
                elif(j is n-1):
                    if(DFS_BT(matrix,i+1,0,Visited,n,count+1)!=-1):
                        flag=1
                        break
                else:
                    if(DFS_BT(matrix,i,j+1,Visited,n,count+1)!=-1):
                        flag=1
                        break
            matrix[i][j]=0
            Visited[k-1]=False

    if (flag is 0):
        return -1
    else:

        return maxii

def constraintgraph(n):
    adjList=[]
    for i in range(n*n):
        l=[]
        l.append(i)
        row=i//n
        column=i%n
        for k in range(n):
            if(k is column):
                continue
            else:
                l.append(row*n+k)
        for k in range(n):
            if(k is row):
                continue
            else:
                l.append(column+n*k)
        if(row==column):
            for k in range(n):
                no=k*n+k
                if(no==k):
                    continue
                else:
                    l.append(no)
        if(row==n-1-column):
            for k in range(n):
                no=k*n+(n-1-k)
                if(no==k):
                    continue
                else:
                    l.append(no)

        adjList.append(l)
    return adjList



def changeDomain(dicti,n,i,j,val,Visit):
    sum=(n*(n*n+1))/2
    for o in range(n*n):
        if(Visit[o] is 0):
            if val in dicti[o+1]:
                dicti[o+1].remove(val)
    #
    newsum=sum
    count=0
    for o in range(n):
        Number=i*n+o
        if(Visit[Number] is not 0):
            count=count+1
            newsum=newsum-Visit[Number]
    count=n-count-1
    for o in range(n):
        Number=i*n+o
        if(Visit[Number] is 0):
            lo=0
            max=len(dicti[Number+1])
            while(lo<max):
                #print(dicti[Number+1][lo])
                if(dicti[Number+1][lo]>(newsum-count)):
                    del dicti[Number+1][lo]
                    max=max-1
                    continue
                lo=lo+1

    #
    newsum=sum
    count=0
    for o in range(n):
        Number=o*n+j
        if(Visit[Number] is not 0):
            count=count+1
            newsum=newsum-Visit[Number]
    count=n-count-1
    for o in range(n):
        Number=o*n+j
        if(Visit[Number] is 0):
            lo=0
            max=len(dicti[Number+1])
            while(lo<max):
                #print(dicti[Number+1][lo])
                if(dicti[Number+1][lo]>(newsum-count)):
                    del dicti[Number+1][lo]
                    max=max-1
                    continue
                lo=lo+1

        #diagonal




def MRV(dicti,Visit,m,n):
    min=1000
    value=0
    flag=0
    for i in range(0,m):
        if(Visit[i] is 0):
            flag=1
            if(min>len(dicti[i+1])):
                min=len(dicti[i+1])
                value=i
    if(flag is 0):
        return -2
    '''adlist=constraintgraph(n)
    current=0
    for i in range(m):
        if(len(dicti[i+1])==min):
            if(len(adlist[i])>current):
                value=i
                current=len(adlist[i])'''

    return value


def DFS_BT_MRV(matrix,i,j,n,dicti,Visit):
    global total
    total=total+1
    flag=0
    num=i*n+j
    dictionary=deepcopy(dicti)
    for k in dicti[i*n+j+1]:
            #print()
            #print("hello",k)
            matrix[i][j]=k
            Visit[num]=k
            changeDomain(dicti,n,i,j,k,Visit)

            if(sumConstraint(matrix)==True):
                #print("abhi")
                x=MRV(dicti,Visit,n*n,n)

                if(x is -2):
                    #print("yes")
                    return 0
                else:
                    #print(x%n)
                    if(DFS_BT_MRV(matrix,x//n,x%n,n,dicti,Visit)!=-1):
                        flag=1
                        break
            dicti=deepcopy(dictionary)
            Visit[num]=0
            matrix[i][j]=0
    if (flag is 0):
        return -1
    else:

        return total



def Square(n):# from geeks for geeks
    magicSquare = [[0 for x in range(n)]
                      for y in range(n)]

    i = n / 2
    j = n - 1
    num = 1
    while num <= (n * n):
        if i == -1 and j == n: # 3rd condition
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1
    return magicSquare
