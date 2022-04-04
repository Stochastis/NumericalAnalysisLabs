import math


def compSimp(a, b, n, f):
    h = (b - a) / n
    xi1 = f(a) + f(b)       # The first and last term of the sum
    xi2 = 0                 # The terms of coefficient 2
    xi4 = 0                 # The terms of coefficient 4
    for i in range(1, n):   # Computing the sums
        x = a + i*h
        if (i % 2 == 0):
            xi2 += f(x)
        else:
            xi4 += f(x)
    return (h/3) * (xi1 + 2*xi2 + 4*xi4)


print("Test 1.a:")
def function(x): return x**3 - 3*x**2 - 8


print("n = 2: %f \nn = 8: %f \nn = 64: %f" %
      (compSimp(0, 4, 2, function), compSimp(0, 4, 8, function), compSimp(0, 4, 64, function)))

print("Test 1.b:")
def function(x): return math.e**x


print("n = 2: %f \nn = 4: %f \nn = 8: %f" %
      (compSimp(0, 4, 2, function), compSimp(0, 4, 4, function), compSimp(0, 4, 8, function)))

print("Test 1.c:")
def function(x): return (100 / (x**2)) * math.sin(10 / x)


print("n = 176: %f" %
      (compSimp(1, 3, 176, function)))
