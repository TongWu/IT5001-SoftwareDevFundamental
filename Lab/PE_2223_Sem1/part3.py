from pprint import pprint

def str_to_two_d(pic):
    num = []
    for element in pic:
        num.append(list(element))
    return num

def two_d_to_str(pic):
    num = []
    for lines in pic:
        str1 = ''
        for char in lines:
            str1 += char
        num.append(str1)
    return num

'''
# for your testing
def mTightPrint(m):
    for row in m:
        print(''.join(row))
'''

def pic_diff(pic1,pic2):
    row_1 = len(pic1)
    row_2 = len(pic2)
    col_1 = len(pic1[0])
    col_2 = len(pic2[0])
    result = []
    if row_1 == row_2 and col_1 == col_2:
        for i in range(len(pic1)):
            str1 = ''
            for j in range(len(pic1[0])):
                if pic1[i][j] == pic2[i][j]:
                    str1 += '='
                else:
                    str1 += 'X'
            result.append(str1)
    else:
        for i in range(max(row_1, row_2)):
            str1 = ''
            for j in range(max(col_1, col_2)):
                pic1_bool = True
                pic2_bool = True
                try:
                    test1 = pic1[i][j]
                except IndexError:
                    pic1_bool = False
                try:
                    test2 = pic2[i][j]
                except IndexError:
                    pic2_bool = False
                if not (pic1_bool or pic2_bool):
                    str1 += '0'
                elif not pic2_bool:
                    str1 += '1'
                elif not pic1_bool:
                    str1 += '2'
                elif pic1[i][j] == pic2[i][j]:
                    str1 += '='
                else:
                    str1 += 'X'
            result.append(str1)

    return result

def count_cells(pic):
    return -1
   

# These are some sample pic for you in string formats
pic1 = ['##########', '##..######', '#....#####', '#....##.##', '##..##...#', '#######.##']
pic1b = ['##########', '##..######', '#....#####', '##..###.##', '######...#', '#######.##']
pic1c = ['#############', '##..#########', '#....########', '##..###.#####', '######...####']
pic2 = ['#################', '##....###########', '#......##########', '#......####..####', '##....####....###', '###########..####', '###.#############', '##...############', '###.###########..', '##############...']
pic2b = ['#################', '###..############', '##....#####...###', '##....####.....##', '###..#####.....##', '###########...###', '####.############', '###...###########', '####.##########..', '##############...']
pic3 = ['..###########', '##..#####..##', '#....###....#', '##..###.#..##', '######...####', '######...####', '#######.#####']
# remember NOT to submit them to your Coursemology submission

#pprint(pic1)
pprint(pic_diff(pic1, pic1b))

