from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
from math import pi

def trapezoidal(f, a=0, b=1, n=100):
    h = (b-a)/n
    S = 0
    for i in range(1, n+1):
        S += (h/2)*(f(a+(i-1)*h) + f(a+i*h))
    return S

def question1(x):
    return math.sin(x)

def question2(x):
    return 4/(1+x**2)

def question3(x):
    return (pi**(1/2)*math.exp(-x**2))


print(trapezoidal(question1, 0, math.pi/2, 50))
print(trapezoidal(question2, 0, 1, 100))
print(trapezoidal(question3, -100, 100, 1000))