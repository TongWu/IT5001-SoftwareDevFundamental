import time
import sys


def nChooseK(n, k):
    # Consider all situations
    # If k is greater than n or a negative number, the computing is impossible
    if k > n or k < 0:
        return 0

    # nC0 or nCn is always 1
    if k == 0 or k == n:
        return 1

    # Maximise the efficiency
    # nCk is equvalient to nC(n-k)
    k = min(k, n - k)

    # Compute pascal's triangle
    row = [0] * (k + 1)
    row[0] = 1

    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            row[j] = row[j] + row[j - 1]
            j -= 1
    return row[k]  # change the code here


def maxNWithinOneMinute():
    n = 21000
    current_result = 0
    start_time = time.time()
    current_result = nChooseK(n, n // 2)
    print(n)
    print(time.time() - start_time)
    print(len(str(current_result)))
    print(current_result)

maxNWithinOneMinute()