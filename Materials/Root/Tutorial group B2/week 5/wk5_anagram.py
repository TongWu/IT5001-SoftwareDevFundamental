#strategy is to create two dictionaries of characters and check
#if the two dictionaries are the same
def anagram(str1, str2):
    dict1 = {}
    dict2 = {}
    for i in str1:
        #checks whether i exists in dict already
        if i not in dict1:
            #creates entries if it doesn't exist
            dict1[i] = 1

        else:
            #increment entry otherwise
            dict1[i] += 1

    for i in str2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1

    #to account for different spaces
    dict1[" "] = 0
    dict2[" "] = 0

    return dict1 == dict2
