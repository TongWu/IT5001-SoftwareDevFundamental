parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben',
          'Ben':'Howard', 'Howard':'George', 'Frank':'Amy',
            'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill',
          'Zoe':'Mary'}


def is_ancestor(name1,name2,parent): # check if name1 is an ancestor of name2
    return 

def is_related(name1,name2,parent):
    return

print("Is Mary an ancestor of Simon?")
print(is_ancestor('Mary','Simon',parent))
print("Is Zoe an ancestor of Joe?")
print(is_ancestor('Zoe','Joe',parent))
print()

'''
print("Is Joe is_related to Philip?")
print(is_related('Joe','Philip',parent))
print("Is Amy is_related to May?")
print(is_related('Amy','May',parent))
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))    
print()


parent['Ben']='Philip' #modify the dictionary so that Philip is Ben's parent
print("After Philip became Ben\'s parent...")
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))
'''
