def fragment(filename,word):
    lst = []
    result = []
    with open(filename) as f:
        for line in f:
            lst.append(line.rstrip('\n'))
        for i in range(len(word)):
            if word[:i] in lst:
                first = word[:i]
                if word[i:] in lst:
                    second = word[i:]
                    result.append((first, second))
    return result

#print(fragment('fragment_simple.txt','umbrella'))
print(fragment('fragment_all3.txt','board'))



