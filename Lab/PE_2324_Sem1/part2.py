def prefix(s1, s2):
    min_len = min(len(s1), len(s2))
    is_prefix = False
    for i in range(min_len-1):
        if s1[i] == s2[i]:
            is_prefix = True
        else:
            is_prefix = False
    return is_prefix


# Test case
print(prefix('abc', 'abcdz'))
print(prefix('abc', 'kkkabc'))
print(prefix('xyzabc', 'xyz'))

def check_prefix(seq):
    ptr1 = 0
    ptr2 = len(seq)-1
    is_prefix = None
    while ptr2 >= 0:
        min_len = min(len(seq[ptr1]), len(seq[ptr2]))
        if ptr1 == ptr2:
            break
        for i in range(min_len-1):
            if seq[ptr1][i] != seq[ptr2][i]:
                is_prefix = False
        if is_prefix is None:
            return True
        ptr1 += 1
        ptr2 -= 1
    return is_prefix