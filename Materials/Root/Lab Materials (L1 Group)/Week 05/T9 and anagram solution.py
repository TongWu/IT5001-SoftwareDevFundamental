keyD = {' ': 0, 'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}
keyL = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def is_anagram(word1, word2):
    #idea is to have 2 dictionaries to count how many occurences of each
    #character in each word
    dict1 = {}
    dict2 = {}

    #create entry if character not already seen,
    #else just increment the count
    for i in word1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    for i in word2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1

    return dict1 == dict2


def to_dict(keyL):
    keyD = {}
    for i in range(len(keyL)):
        #i is the index and also the button number
        for j in keyL[i]:
            #loop through each character in the string and assign
            #to current button number
            keyD[j] = i
    return keyD

def to_list(keyD):
    #use .values() to get the biggest number in values
    #then we create an empty list with the appropriate length
    #we add 1 because if we need to account for 0
    keyL = [""] * (max(keyD.values()) + 1)

    for k,v in keyD.items():
        #we index using values then just add the key to the string
        keyL[v] = keyL[v] + k

    return keyL

def to_nums(word):
    out = ""
    for i in word:
        out += str(keyD[i])

    return int(out)


#CREDITS TO SEAH BEI YING FROM GROUP 4
def to_letters(num):
    #go through each character in num and find all possible words
    #then append them into a list
    words = [""]
    for lnum in str(num):
        lnum = int(lnum)
        nwords = []
        if lnum == 1:
            continue
        for word in words:
            for char in keyL[lnum]:
                nwords.append(word + char)
        words = nwords
    return words
    
