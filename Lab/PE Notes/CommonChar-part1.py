def common_char_i(name1,name2):
    count = 0
    for i in range(min(len(name1), len(name2))):
        if name1[i].lower() == name2[i].lower():
            count += 1
    return count

def common_char_r(name1,name2):
    count = 0
    if min(len(name1), len(name2)) == len(name1):
        min_name = name1
        max_name = name2
    else:
        min_name = name2
        max_name = name1
    if not min_name:
        return 0
    if min_name[0].lower() == max_name[0].lower():
        count += 1
    return count + common_char_r(min_name[1:], max_name[1:])
def common_char_u(name1,name2):
    return sum(1 for a, b in zip(name1.lower(), name2.lower()) if a == b)

# for your testing out
# Do not include them in your submission
'''
print(common_char_i('Mark','Mary'))
print(common_char_i('Brandy','Flank'))
print(common_char_i('Larry','Clark'))
print(common_char_i('Teddy','Andy'))
print(common_char_i('McDonald','Andrey'))

print(common_char_r('Mark','Mary'))
print(common_char_r('Brandy','Flank'))
print(common_char_r('Larry','Clark'))
print(common_char_r('Teddy','Andy'))
print(common_char_r('McDonald','Andrey'))
'''
print(common_char_u('Mark','Mary'))
print(common_char_u('Brandy','Flank'))
print(common_char_u('Larry','Clark'))
print(common_char_u('McDonald','Andrey'))
print(common_char_u('Teddy','Andy'))

