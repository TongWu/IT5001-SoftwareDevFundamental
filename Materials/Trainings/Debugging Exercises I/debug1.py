def p1(x, y):
    return p2(x, y) + p3(x, y)

def p2(z, w):
    return z * w

def p3(a, b):
    return p2(a) + p2(b)
