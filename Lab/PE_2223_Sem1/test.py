a = 'audhaw1'
result = ''
for char in a:
    if char.isalpha():
        result += ''.join([char])

print(result)