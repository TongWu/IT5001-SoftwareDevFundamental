def checkered_flag(r,c,s):
    result = [[',' for _ in range(c)] for _ in range(r)]
    count = s

    for i in range(len(result)):
        count_j = s
        if count>0:
            for j in range(len(result[0])):
                if count_j > 0:
                    result[i][j] = '#'
                    count_j -= 1
                else:
                    count_j -= 1
                    if count_j == -s:
                        count_j = s
            count -= 1
        else:
            count -= 1
            if count == -s:
                count = s
            count_j = 0
            for j in range(len(result[0])):
                if count_j > 0:
                    result[i][j] = '#'
                    count_j -= 1
                else:
                    count_j -= 1
                    if count_j == -s:
                        count_j = s
    return result

# Test case
#from pprint import pprint
#pprint(checkered_flag(8,10,3))

def black_area(r,c,s):
    painted = checkered_flag(r,c,s)
    count = 0
    for i in painted:
        count += i.count('#')
    return count

# Test case
#print(black_area(8,10,3))