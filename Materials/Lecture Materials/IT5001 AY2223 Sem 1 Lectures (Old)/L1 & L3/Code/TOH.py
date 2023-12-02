towers = [[3,2,1],[],[]]

#towers = [[6,5,4,3,2,1],[],[]]

def solve(towers):
    move(towers,len(towers[0]),0,len(towers)-1)
    

def move(towers,num_piece,source, dest):
    if num_piece == 1:
        temp = towers[source].pop()
        towers[dest].append(temp)
        print('Move Piece {} from Pos {} to Pos {}.'.format(temp,source,dest))
        print_towers(towers)
        print()
        print()
    else:
        other = 3 - source - dest
        move(towers,num_piece-1,source,other)
        move(towers,1,source, dest)
        move(towers,num_piece-1,other,dest)

def print_towers(towers):
    max_h = 0
    for i in towers:
        if len(i) > max_h:
            max_h = len(i)

    for line in range(max_h-1,-1,-1):
        s = ' '
        for t in range(0,len(towers)):
            if len(towers[t]) > line:
                s += str(towers[t][line])
            else:
                s += ' '
            s += ' '

        print (s)

    print('-'+'+-'*len(towers))
        
        
print_towers(towers)        
solve(towers)      

    
