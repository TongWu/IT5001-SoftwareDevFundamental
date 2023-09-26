

def createZeroMatrix(r,c):
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

def printTTT(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print( '-----')
piece = ['X','O']

def checkValidMove(game,inp):
    # Check the move position is in the matrix
    matrix_row = 3
    matrix_col = 3
    inp_row = (inp-1) // matrix_row
    inp_col = (inp-1) % matrix_col
    if inp_row > (matrix_row-1) or inp_row < 0 or inp_col > (matrix_col-1) or inp_col < 0:
        return False
    # Then check the position has been taken
    elif game[inp_row][inp_col] == 'X' or game[inp_row][inp_col] == 'O':
        return False
    else:
        return True

def checkWin(game):
    # Has different wins method:
    # 1. Same row with same sign
    for row in game:
        if row[0] == row[1] == row[2]:
            return row[0]
    # 2. Same column with same sign
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col]:
            return game[0][col]
    # 3. Diagonal with same sign
    if game[0][0] == game[1][1] == game[2][2]:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0]:
        return game[0][2]
    # Return False if no winner
    return False

def tttGamePlay():
    game = createZeroMatrix(3,3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0

    printTTT(game)
    for i in range(9): # Anyhow play 9 times
        print()
        pos = int(input(f'Player {piece[player]} move:')) - 1
        while not checkValidMove(game, pos+1):
            print('Invalid move!')
            pos = int(input(f'Player {piece[player]} move:')) - 1
        game[pos//3][pos%3] = piece[player]
        player = 1 - player
        printTTT(game)
        if not checkWin(game):
            pass
        else:
            print('Player ' + checkWin(game) + ' won!')
            break

    return True

game1 = [[1,2,3],[4,5,6],[7,8,9]]
game2 = [['X',2,3],['X',5,6],['X',8,9]]
game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
game5 = [['X','X','O'],['X','O','X'],['O','X','X']]

'''
print(checkWin(game1))
print(checkWin(game2))
print(checkWin(game3))
print(checkWin(game4))
print(checkWin(game5))
'''

tttGamePlay()

# print(checkValidMove(game2, 4))