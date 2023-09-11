import random


def monte_carlo_pi(n):
    # radius
    r = 1
    # hit
    inside_num = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        if (x ** 2 + y ** 2 <= r ** 2):
            inside_num += 1

    pi_est = 4 * (inside_num / n)
    return pi_est  # write your code here


print(monte_carlo_pi(10000))