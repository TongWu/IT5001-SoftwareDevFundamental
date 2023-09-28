def fizz_i(factor, n):
    result = []
    for i in range(1, n + 1):
        if i % factor == 0:
            result.append('Fizz')
        else:
            result.append(i)
    return result


def fizz_r(factor, n):
    if not n:
        return []
    if n % factor == 0:
        result = 'Fizz'
    else:
        result = n
    return fizz_r(factor, n - 1) + [result]


fizz_l = lambda factor, n: ['Fizz' if i % factor == 0 else i for i in range(1, n + 1)]


def fizzbuzz(factor1, factor2, n):
    result = []
    for i in range(1, n + 1):
        if i % factor1 == 0 and i % factor2 != 0:
            result.append('Fizz')
        elif i % factor1 != 0 and i % factor2 == 0:
            result.append('Buzz')
        elif i % factor1 ==0 and i % factor2 == 0:
            result.append('FizzBuzz')
        else:
            result.append(i)
    return result


print(fizzbuzz(3,4,13))
