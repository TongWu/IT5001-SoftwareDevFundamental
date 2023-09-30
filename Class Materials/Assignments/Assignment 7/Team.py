from random import randint
from Characters import *

def randAlive(team): # return a random member in the team that is alive
    #But we assume that someone must be alive in the team
    n = len(team)
    r = randint(0,n-1)
    return r if team[r].alive else randAlive(team)

def randDeath(team): # return a random member in the team that is dead
    #But we assume that someone must be dead in the team
    n = len(team)
    r = randint(0,n-1)
    return r if not team[r].alive else randDeath(team) 




def allDead(team): # Check if all the team is dead
    for i in team:
        if i.alive:
            return False
    return True

def allAlive(team):# Check if all the team is alive
    for i in team:
        if not i.alive:
            return False
    return True


lenLongestName = 11
# The length of the longest name. Just for the printing format

def printStat(team): # Print a team in a nice format
    
    if team == []:
        print("(Currently no member in the team now)")
        return
    names = 'Members:   '
    hp =    'Hitpoints: '
    sth  =  'Strength:  '
    maxm =  'Max. Mana: '
    mana =  'Currnet M: '
    for i in team:
        nspace = lenLongestName - len(i.name)
        names += '|' + ' '*nspace   +i.name
        nspace = lenLongestName - len(str(i.hp))
        hp += '|' + ' '*nspace  + str(i.hp)
        if i.str:
            nspace = lenLongestName - len(str(i.str))
            sth += '|' + ' '*nspace  + str(i.str)
        else:
            sth += '|' + ' '*lenLongestName
        if i.maxmana:
            nspace = lenLongestName - len(str(i.maxmana))
            maxm += '|' + ' '*nspace  + str(i.maxmana)
        else:
            maxm += '|' + ' '*lenLongestName
            
        if i.mana:
            nspace = lenLongestName - len(str(i.mana))
            mana += '|' + ' '*nspace  + str(i.mana)
        else:
            mana += '|' + ' '*lenLongestName            
    print(names)
    print(hp)
    print(sth)
    print(maxm)
    print(mana)
        


