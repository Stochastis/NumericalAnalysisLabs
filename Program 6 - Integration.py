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

# Recursive Adaptive Simpson's Rule Starter


def adaptiveStart(a, b, f, Tol, N):
    return adaptive(a, b, f, 10*Tol, N, 1)

# Recursive Adaptive Simpson's Rule


def adaptive(a, b, f, Tol, N, L):
    if L > N:
        return "Max Depth Exceeded"
    else:
        h = (b - a) / 2
        fa = f(a)
        fc = f(a + h)
        fb = f(b)
        s = (h / 3) * (fa + 4*fc + fb)
        fd = f(a + h/2)
        fe = f(a + ((3*h) / 2))
        s1 = (h / 6) * (fa + 4*fd + fc)
        s2 = (h / 6) * (fc + 4*fe + fb)
        if abs(s1 + s2 - s) < Tol:
            return s1 + s2
        else:
            left = adaptive(a, a + h, f, Tol/2, N, L + 1)
            right = adaptive(a + h, b, f, Tol/2, N, L + 1)
            if left == "Max Depth Exceeded" or right == "Max Depth Exceeded":
                return "Max Depth Exceeded"
            else:
                return left + right


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


print("n = 176: %f\n" %
      (compSimp(1, 3, 176, function)))

print("Test 2.a:")
def function(x): return x**3 - 3*x**2 - 8


print(str(adaptiveStart(0, 4, function, 1e-7, 2)) + "\n")

print("Test 2.b:")
def function(x): return math.e**x


print(adaptiveStart(0, 4, function, 1e-4, 2) + "\n")

print("Test 2.c:")
def function(x): return (100 / (x**2)) * math.sin(10 / x)


print(adaptiveStart(1, 3, function, 1e-4, 100))
