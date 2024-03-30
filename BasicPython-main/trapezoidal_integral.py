from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def trapezoidal(f, a, b, N):
    h = (b-a)/N
    S = 0
    for i in range(1, N+1):
        S += (h/2)*(f(a+(i-1)*h) + f(a+i*h))
    return S

result = trapezoidal(sin, 0, math.pi/2, 100)
print(result)