from pprint import pprint

def clean_text(filename,minlen):
    result1 = []
    with open(filename, encoding='UTF-8') as f:
        for lines in f:
            result = ''
            for char in lines:
                if char.isalpha():
                    result += ''.join([char])
                else:
                    result += ''.join([' '])
            temp = result.rstrip('\n').split()
            for item in temp:
                try:
                    if not item.isalpha():
                        pass
                    elif len(item) <= minlen:
                        pass
                    else:
                        result1.append(item.lower())
                except TypeError:
                    pass
    return result1

def text_analytics(text,n):
    temp = {}
    result = {}
    final = {}
    for items in text:
        if items not in temp:
            temp[items] = 1
        else:
            temp[items] += 1
    for pair in temp.items():
        if pair[1] not in result:
            result[pair[1]] = {pair[0]}
        else:
            result[pair[1]].add(pair[0])
    for i in range(1, n+1):
        key1 = max(result.keys())
        final[key1] = result.pop(key1)
    return final


m = clean_text('gruffalo.txt', 4)

print(text_analytics(m, 5))