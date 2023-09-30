def plinko_i(seq,b,m,s):
    big = 0
    middle = 0
    small = 0
    for element in seq:
        if element == 0:
            big += 1
        elif element == 1:
            middle += 1
        elif element == 2:
            small += 1
        sum = big + middle + small
        if big >= b or middle >= m or small >= s:
            return sum
    return 0

# print(plinko_i((0,0,0,0,0,0,1,2),6,2,2))
#print(plinko_i((1,1,2,2,0,2,0,1,2,1),2,3,5))

def plinko_r(seq,b,m,s):
    if seq[0] == 0:
        b -= 1
    elif seq[0] == 1:
        m -= 1
    elif seq[0] == 2:
        s -= 1
    if b==0 or m==0 or s==0:
        return 1
    return 1+plinko_r(seq[1:], b, m, s)

#print(plinko_r((0,0,0,0,0,1,0,1,2),6,2,2))
#print(plinko_r((1,1,2,2,0,2,0,1,2,1),2,3,5))

def plinko_general(seq,prizes):
    # Convert the prizes tuple to a list for mutability
    prizes= list(prizes)
    count = 0
    for slot in seq:
        # Decrease the prize count for the corresponding slot
        prizes[slot] -= 1
        count += 1
        if prizes[slot] == 0:
            return count

        
print(plinko_general((0,0,0,0,0,1,0,1,2),(6,2,2)))
