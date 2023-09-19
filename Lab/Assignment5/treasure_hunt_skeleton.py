d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', '2': '.', '4': '.', 'B': '^', '+': '^',
      ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ',
      '|': ' ', '#': ' '}
d2 = {'C': 'W', '3': 'W', 'F': 'W', '0': 'T', '2': 'T', '4': 'T', 'B': '.', '+': '.', ';': '.', 'Q': '^', '7': '^',
      '8': '^', 'D': 'E', '1': 'E', 'Z': 'E', '(': 'M', ')': 'M', '9': 'M', '*': ':', '|': ':', '#': ':', 'X': ' ',
      'P': ' ', '!': ' '}


def decode_map(mapfile, ddict, outfile):
    # open two files, one for input and one for output
    with open(mapfile, 'r') as infile, open(outfile, 'w') as outfile:
        # read each line
        for l in infile:
            # de-code each character in the line
            translated_line = ""
            for char in l:
                if char in ddict:
                    translated_line += ddict[char]
                else:
                    translated_line += char
            outfile.write(translated_line)


def find_treasure(mapfile):
    # open file
    with open(mapfile, 'r') as infile:
        # read number of lines
        lines = infile.readlines()
        # for each line and each character
        for i in range(1, len(lines)-1):
            for j in range(len(lines[i])-1):
                # find a shape of cross shape with 'T'
                if lines[i-1][j] == 'T' and \
                        lines[i][j-1] == 'T' and \
                        lines[i][j] == 'T' and \
                        lines[i][j+1] == 'T' and \
                        lines[i+1][j] == 'T':
                    return (i, j)
    return None


print("Map 1")
decode_map('encoded_map.txt', d1, 'decoded_map.txt')
print(find_treasure('decoded_map.txt'))

# Uncomment the following for your test cases
print("Map 2")
decode_map('encoded_map2.txt', d1, 'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt', d1, 'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt', d1, 'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt', d2, 'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))
