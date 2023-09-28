def createZeroMatrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
        
def PDMap(r,c,sites):
    # Create a empty map
    pizza_map = createZeroMatrix(r, c)
    row_num = -1
    # For each element
    for row in pizza_map:
        row_num += 1
        for col in range(c):
            distance = []
            # Calculate each store distance
            for cor in sites:
                distance.append(sqrt(abs(row_num-cor[0]) ** 2 + abs(col-cor[1]) ** 2))
            # Find min distance and min store count
            min_dis = min(distance)
            count_min = sum(1 for x in distance if x == min_dis)
            if count_min == 1:
                pizza_map[row_num][col] = distance.index(min_dis)
            else:
                # Return x if multiple stores
                pizza_map[row_num][col] = 'X'
    return pizza_map


def sqrt(x, tolerance=1e-10, max_iterations=1000):
    """
    Newton-Raphson Method of squared root
    :param x: numbers need to sqrt
    :param tolerance: threshold value
    :param max_iterations: maximum iterations
    :return: squared root of x
    """

    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")

    if x == 0 or x == 1:
        return x

    guess = x / 2.0
    for _ in range(max_iterations):
        next_guess = (guess + x / guess) / 2.0
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess

    return guess


#mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
# PDMap(60,70,[[10,20],[30,20],[40,50]])
#ex = PDMap(60,70,[[10,20],[30,20],[40,50]])
    
