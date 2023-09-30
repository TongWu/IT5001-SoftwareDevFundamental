
def createZeroMatrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
        
def PDMap(r,c,sites):
    return

#mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))

mTightPrint(PDMap(60,70,[[10,20],[30,20],[40,50]]))
ex = PDMap(60,70,[[10,20],[30,20],[40,50]])
    
