import math

a = 1 #548
b = 2 #753
c = -3 #162784

delta = b * b - 4 * a * c

s1 = (-b - math.sqrt(delta)) / (2 * a)
s2 = (-b + math.sqrt(delta)) / (2 * a)

print("Solution 1: x = ", s1)
print("Solution 2: x = ", s2)
