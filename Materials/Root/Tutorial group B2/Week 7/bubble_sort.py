def bubbleSort(lst):
    swapped = False
    for j in range(len(lst)):
        swapped = False
        for i in range(len(lst)-j-1):
            if lst[i] > lst[i+1]:
                temp  = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapped = True
        if not swapped:
            break

    return lst
