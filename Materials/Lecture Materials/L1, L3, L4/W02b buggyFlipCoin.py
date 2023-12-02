import random

def flipCoins():
    print('I will flip a coin 1000 times. ')
    print('Guess how many times it will come up heads. ')
    flips = 0
    heads = 0
    while flips < 1000:
        coin = random.randint(0, 1) 
        if coin == 1:
            heads = heads + 1
            flips = flips + 1            
        if flips == 500:
            print('Half way done, and heads has come up ' + str(heads) + ' times.')
    print()
    print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')


flipCoins()
