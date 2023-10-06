def three_sum(lst, target):
    ptr1 = 0
    s = set(lst)
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            t_num = target - lst[i] - lst[j]
            if t_num in lst and j < lst.index(t_num):
                result.append((lst[i], lst[j], t_num))
    return result

print(three_sum([4,3,1,2,7,8,5,9],10))