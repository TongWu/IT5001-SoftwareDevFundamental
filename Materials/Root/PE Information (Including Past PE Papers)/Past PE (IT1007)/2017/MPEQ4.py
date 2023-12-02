error = 0.00000001


def f(x):
    return (x/40)**5 - 8*(x/40)**3 + x/4 + 6


def bisection(start,end):
    return 0 # change your code here, your function should return x
             # such that abs(f(x)) < error

ans = bisection(-100,80)

print('Final answer = ' + str(ans))
print('And f(x) is ' + str(f(ans))) # Should be very close to zero
              # and the absoulte value will be smaller than 'error'
