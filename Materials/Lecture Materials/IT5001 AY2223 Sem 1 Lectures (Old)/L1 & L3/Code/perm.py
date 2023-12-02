from pprint import pprint
L = list('pspr')
'''
[1,3,2]
[2,1,3]
[1,2,3]
[2,3,1]
[3,1,2]
[3,2,1]
'''
def permutate(L):
    if L == []:
        return [[]]
    output = []
    for x in L:
        L2 = L.copy()
        L2.remove(x)
        rest_perm = permutate(L2)
        round_list = [[x]+l for l in rest_perm]
        output.extend(round_list)
    return output

#pprint([''.join(x) for x in permutate(L)])

def decompose_factor(N):
    factor = 2
    output ={}
    while N>1:
        if N%factor == 0:
            if not factor in output:
                output[factor] = 0
            output[factor] += 1
            N //= factor
        else:
            factor += 1
    return output

N = 2**100 - 1
print("The factors of ", N, decompose_factor(N))
def LCM(lst):
    factors = decompose_factor(lst[0])
    for n in lst[1:]:
        fn2 = decompose_factor(n)
        for k,v in fn2.items():
            if not k in factors.items():
                factors[k] = v
            else:
                factors[k] = max(factors[k],v)
    lcm = 1
    for k,v in factors.items():
        lcm *= k**v
    return lcm

'''
import time    
li= [i for i in range(3,250000,5)]
start = time.time()
print(LCM(li))
print(str(time.time()-start))

'''
