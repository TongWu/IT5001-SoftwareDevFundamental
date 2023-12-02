#keyL =[" ", "", "abc", "def", "ghi", "jkl", "mno","pqrs", "tuv", "wxyz"]
#keyD = {' ': 0, 'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}
def to_dict(keyL):
    dict1 = {}

    #go through each element in list with i as the index
    for i in range(len(keyL)):
        #some elements might have more than one char so need to loop again
        for ele in keyL[i]:
            #set char as key and index as value
            dict1[ele] = i

    return dict1

def to_list(keyD):
    #create a list of empty strings of the appropriate length
    #find this length by finding the max value
    output = [""]*(max(keyD.values())+1)

    #use the .items() function to iterate through each key-value pair
    #assign the key to the appropriate index
    #can use + operator since all are strings
    for keys, values in keyD.items():
        output[values] += keys
    return output

def to_nums(word):
    output = ""

    #loop through the word and check the value using dictionary
    for i in word:
        output += str(keyD[i])
    return output

def to_letters(num):
    words = [""]

    #loop through individual numbers in num
    for lnum in str(num):
        lnum = int(lnum)
        #if lnum represents nothing then continue
        if not keyL[lnum]:
            continue
        nwords = []

        #append the character to each preexisitng word
        for word in words:
            for char in keyL[lnum]:
                nwords.append(word + char)
            words = nwords
    return words
print(to_letters(293))
        
