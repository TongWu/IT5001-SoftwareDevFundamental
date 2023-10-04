from Characters import *
from random import randint
from Team import *


# You increase nCharType one at a time 
nCharType = 5 # no. of types of characters you can choose
gold = 800    # Gold for you to recruit characters
minCost = 100 # A hack for userChooseTeam()

'''
Type:
1: Fighter (Given)
2: Mage (Given)
3: Berserker 
4: ArchMage
5: Necromancer
'''



def createChar(i):
    if i == 1:
        return Fighter()
    elif i == 2:
        return Mage()
# You should uncomment the following to test one by one
    elif i == 3:
        return Berserker()
    elif i == 4:
        return ArchMage()
    elif i == 5:
        return Necromancer()


def createRandTeam(gold):
    team = []
    while gold > 0:
        tempChar = createChar(randint(1,nCharType))
        if gold >= tempChar.cost:
            gold -= tempChar.cost
            team.append(tempChar)       
    return team

def userChooseTeam(gold):
    team = []
    choice = -1
    while (gold >= minCost) and (gold != 0) :
        print("\nYour current team:")
        printStat(team)
        print(f'\nYou have {gold} gold currently')
        choice = -1
        while choice < 1 or choice > nCharType:
            print("Choices:")
            print(f"1: Fighter (cost: {Fighter().cost})")
            print(f"2: Mage (cost: {Mage().cost})")
# You should uncomment the following to test one by one            
            print(f"3: Berserker (cost: {Berserker().cost})")
            print(f"4: ArchMage (cost: {ArchMage().cost})")
            print(f"5: Necromancer (cost: {Necromancer().cost})")
            choice = int(input(f'Input a choice from 1 to {nCharType}:'))
            if choice < 1 or choice > nCharType:
                print(f"Your choice {choice} is not valid. Please choose again")
        if choice > 0 and choice <= nCharType:
            tempChar = createChar(choice)
            if gold >= tempChar.cost:
                gold -= tempChar.cost
                team.append(tempChar)         
    return team

def runBattle(teamA,teamB, pause = True):
    # Return 0 when Team A win and 1 otherwise.
    # There will be no tie

    rd = 0
    ATurn = True
    dprint("")
    dprint("THE BATTLE STARTS!!!!!")

    while (not allDead(teamA)) and not allDead(teamB):
        dprint('')
        
        if ATurn:
            myTeam = teamA
            enemy = teamB
            rd += 1
            dprint(f'Round {rd}')
        else:
            myTeam = teamB
            enemy = teamA

        if printActionDescription:
            print("Team A:")
            printStat(teamA)
            print()
            print("Team B:")
            printStat(teamB)

        dprint('')
        
        attacker = randAlive(myTeam)
        teamS = 'Team A' if ATurn else 'Team B'
            
        dprint(teamS + f' member {attacker} {myTeam[attacker].name} acts')
        myTeam[attacker].act(myTeam,enemy)
        ATurn = not ATurn
        if pause:
            input("Press Enter to continue....")
        
    if allDead(teamB):
        dprint("Frist team won!")
        return 0
    else:
        dprint("Second team won!")
        return 1


def gameStart(gold,pause = True):
    enemy = createRandTeam(gold)
    print("Your enemy will be:")
    printStat(enemy)
    myTeam = userChooseTeam(gold)
    if runBattle(myTeam,enemy,pause) == 0:
        print("Congraz! You won!")
    else:
        print("Sorry, you lose")


gameStart(gold,False) # The second parameter is to wait for each tern




