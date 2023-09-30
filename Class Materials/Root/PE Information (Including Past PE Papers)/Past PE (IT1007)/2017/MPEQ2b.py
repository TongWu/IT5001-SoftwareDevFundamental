import matplotlib.pyplot as plt
from math import cos,tan

def f1(x):
    return cos(x/10)+tan(x/10)

def f2(x):
    return cos(x/5) * cos(x/50)

def f3(x):
    return (x/40)**5 - 8*(x/40)**3 + x/4 + 6

def plot(x1,x2,f):
    return # change your code here, your function should not return anything


plot(-100,100,f1)
plot(-100,100,f2)
plot(-100,100,f3)


