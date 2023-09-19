parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben',
          'Ben':'Howard', 'Howard':'George', 'Frank':'Amy',
            'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill',
          'Zoe':'Mary'}


def is_ancestor(name1,name2,parent): # check if name1 is an ancestor of name2
    # determine base case
    if name2 not in parent:
        return False
    if parent[name2] == name1:
        return True
    # recursive run, for cross-gen case
    return is_ancestor(name1, parent[name2], parent)

def is_related(name1,name2,parent):
    # Find the ancestor split of the name
    def all_ancestors(name, parent):
        ancestors = set()
        ancestors.add(name) # add self name
        while name in parent:
            name = parent[name]
            ancestors.add(name)
        return ancestors
    split1 = all_ancestors(name1, parent)
    split2 = all_ancestors(name2, parent)
    # If they are related, two set should has any name common
    return bool(split1.intersection(split2))

print("Is Mary an ancestor of Simon?")
print(is_ancestor('Mary','Simon',parent))
print("Is Zoe an ancestor of Joe?")
print(is_ancestor('Zoe','Joe',parent))
print()


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

