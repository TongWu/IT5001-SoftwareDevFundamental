from random import randint
from pprint import pprint

BLOCKED = 1
EMPTY = 0
TRAIL = 9

def createRandomMaze(n,m):
    return [[randint(0,1) for i in range(m)] for j in range(n)]

def createZeroMatrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def distance2(x1,y1,x2,y2):
    return (y2-y1)**2 + (x2-x1)**2

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
def VD(r,c,sites):
    gotZero = True
    m = createZeroMatrix(r,c)
    for i in range(r):
        for j in range(c):
            minD = (r*c)**2
            nearest = -1
            for k in range(len(sites)):
                d2 = distance2(i,j,sites[k][0],sites[k][1])
                if d2 <= minD:
                    if d2 == minD:
                        nearest = 'X'
                    else:
                        minD = d2
                        nearest = k
            m[i][j] = nearest
            
    return m
'''
mTightPrint(VD(50,80,[(20,10), (30,30),(40,20),(45,55),(10,55),(35,70),(35,60)]))
'''        
        
def transpose(m):
    r = len(m)
    c = len(m[0])
    output = createZeroMatrix(c,r)
    for i in range(r):
        for j in range(c):
            output[j][i] = m[i][j]
    return output

def transpose2(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

            
def minorMatrix(m,i,j):
    output = []
    for row in (m[:i]+m[i+1:]):
        output.append(row[:j]+row[j+1:])
    return output

def det(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    output = 0
    for i in range(len(m)):
        output += ((-1)**i) * m[0][i] * det(minorMatrix(m,0,i))
    return output

m = [[6,1,1],[4,-2,5],[2,8,7]]
#pprint(det(m))
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#pprint(det(m))

'''
for i in range(4):
    for j in range(4):
        mTightPrint(minorMatrix(m,i,j))
'''
m = [[1,2,3],[5,6,7],[9,10,11],[13,14,15]]
pprint(transpose(m))
pprint(transpose(transpose(m)))

def matMul(m1,m2):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    if c1 != r2:
        print("Matrices not match")
        return
    output = createZeroMatrix(r1,c2)
    for i in range(r1):
        for j in range(c2):
            cij = 0
            for k in range(c1):
                cij += m1[i][k]*m2[k][j]
            output[i][j] = cij
    return output

m1 = [[1,2,3],[5,6,7],[9,10,11],[13,14,15]]
m2 = [[4,3,2,1,8,1],[1,2,3,4,3,1],[5,6,7,8,1,2]]
m = matMul(m1,m2)

pprint(m)
pprint(minorMatrix(m,3,5))
