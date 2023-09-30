def dial_i(start, seq):
    result = start
    for tup in seq:
        if tup[0] == 'CW':
            result = (result + tup[1]) % 360
        elif tup[0] == 'CCW':
            result = (result - tup[1])
            if result < 0:
                result = 360 - result
    return result


# Test Case
# seq1 = [('CW',40),('CW',100),('CCW',10),('CW',30),('CCW',20),('CW',180)]
# print(dial_i(350, seq1))

def dial_r(start, seq):
    result = start
    if not seq:
        return result
    if seq[0][0] == 'CW':
        result = (result + seq[0][1]) % 360
    elif seq[0][0] == 'CCW':
        result = (result - seq[0][1])
        if result < 0:
            result = 360 - result
    return dial_r(result, seq[1:])


# Test Case
#seq1 = [('CW',40),('CW',100),('CCW',10),('CW',30),('CCW',20),('CW',180)]
#print(dial_r(70, seq1))

def dial_u(start, seq):
    return [(start+tup[1])%360 if tup[0] == 'CW' else (start-tup[1] if start-tup[1]>0 else 360-start+tup[1]) for tup in seq]


# Test Case
#seq1 = [('CW',40),('CW',100),('CCW',10),('CW',30),('CCW',20),('CW',180)]
#print(dial_u(70, seq1))