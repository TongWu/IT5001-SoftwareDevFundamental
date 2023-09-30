def text_compression(text):
    text_list = text.split(' ')
    word_seen = []
    result = ''
    for word in text_list:
        if len(word) == 1:
            word_seen.append(word)
            continue
        if word_seen and type(word) == type('a'):
            if word.title() in word_seen:
                word_seen.append(text_list.index(word.title()) + 1)
                continue
            elif word.lower() in word_seen:
                word_seen.append(text_list.index(word.lower()) + 1)
                continue
            elif word.upper() in word_seen:
                word_seen.append(text_list.index(word.upper()) + 1)
                continue
        if word not in word_seen:
            word_seen.append(word)
        else:
            word_seen.append(text_list.index(word) + 1)
    for word in word_seen:
        result = result + str(word) + ' '

    return result[:-1]


# for your testing out
# Do not include them in your submission

text2 = 'To be or not to be'
text3 = 'Do you wish me a good morning or mean that it is a good morning whether I want not or that you feel good this morning or that it is morning to be good on'
text7 = 'Text compression will save the world from inefficiency Inefficiency is a blight on the world and its humanity'
print(text_compression(text2))
print(text_compression(text3))
print(text_compression(text7))
