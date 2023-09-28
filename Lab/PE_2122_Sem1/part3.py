def nth_day_pw(N):
    if N == 1:
        return 'F'
    if N == 2:
        return 'B'
    first, second = 'F', 'B'
    for _ in range(3, N+1):
        first, second = second, first+second
    return second

'''
for i in range(1,11):
    print(nth_day_pw(i))
'''
print(nth_day_pw(5))
def kth_letter_nth_day_pw(k,n):
    if n == 1:
        return 'F'
    if n == 2:
        return 'B'
    fib = [1, 1]
    for i in range(3, n+1):
        fib.append(fib[-1] + fib[-2])
    while n > 2:
        # If the length of kth is smaller than the previous day's length
        if k <= fib[n-3]:
            n -= 2
            # Now we are searching for the previous day's password
        # If the length of k is larger than the previous day's length,
        # it means that we need to looking for two days before's password
        else:
            # Delete the length from previous day, which is the 2 days before password
            k -= fib[n - 3]
            n -= 1
        print(n,k,fib[n-1])
    if n == 1:
        return 'F'
    else:
        return 'B'

print(kth_letter_nth_day_pw(25,10))
#print(kth_letter_nth_day_pw(3,8))
#print(kth_letter_nth_day_pw(123456789,99999))
#print(kth_letter_nth_day_pw(123456789,9875))