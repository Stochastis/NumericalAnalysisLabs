import math


def Newtons(p0, e, n0):
    i = 1
    p = p0
    while (i <= n0):
        p0 = p
        p = p0 - (f(p0)/ff(p0))
        if abs(p - p0) < e:
            print("Approximation of p: " + str(p))
            print("Approximation of pn-1 " + str(p0))
            print("f(pn) = " + str(f(p)))
            print("Number of iterations: " + str(i) + "\n")
            return
        i += 1
    print("Failure - Max Iterations Reached")
    print("Approximation of p: " + str(p))
    print("Approximation of pn-1: " + str(p0))
    print("f(pn) = " + str(f(p)) + "\n")


def Secant(p0, p1, e, n0):
    i = 2
    fp0 = f(p0)
    fp1 = f(p1)
    while (i <= n0):
        p = p1 - ((fp1 * (p1 - p0)) / (fp1 - fp0))
        if (abs(p - p1) < e):
            print("Approximation of p: " + str(p))
            print("f(pn) = " + str(f(p)))
            print("Number of iterations: " + str(i) + "\n")
            return
        i += 1
        p0 = p1
        fp0 = fp1
        p1 = p
        fp1 = f(p)
    print("Failure - Max Iterations Reached")
    print("Approximation of p: " + str(p))
    print("f(pn) = " + str(f(p)) + "\n")


# # Test cases
# print("Test 1.a\n")
# def f(x): return x**2 + 1
# def ff(x): return 2*x


# Newtons(0.5, 0.0001, 10)

# print("Test 1.b\n")
# def f(x): return math.atan(x)
# def ff(x): return 1 / (1 + x**2)


# Newtons(1.4, 0.0001, 8)

# print("Test 2.a\n")
# def f(x): return (1 / (1 + x**2)) - 1/2
# def ff(x): return -((2*x) / ((x**2 + 1)**2))


# Newtons(2, 0.001, 10)

# print("Test 3.a\n")
# def f(x): return 5*x + 7
# def ff(x): return 5


# Newtons(1000, 0.0001, 100)

# print("Test 3.b\n")
# def f(x): return x**3 + 4*x**2 - 10
# def ff(x): return 3*x**2 + 8*x


# Newtons(1, 0.0001, 20)

# print("Test 4.a\n")
# def f(x): return x**3 + 4*x**2 - 10
# def ff(x): return 3*x**2 + 8*x


# Secant(1, 2, 0.0001, 20)

# print("Test 4.a\n")
# def f(x): return math.cos(x) - x
# def ff(x): return -(math.sin(x)) - 1


# Secant(0.5, math.pi/4, 0.0001, 20)

# Manual Input
def f(x): return (1500/x)*(1 - (1+x)**-360) - 200000


def ff(x): return (x**6 - 6*x**5 + 18*x**4 - 26*x**3 + 18*x**2 - 6*x + 2) / \
    (x**3 * (x**4 - 4*x**3 + 5*x**2 - 2*x + 1) *
     math.sqrt(x**4 - 4*x**3 + 5*x**2 - 2*x + 1))


Newtons(2, 0.00001, 100)
