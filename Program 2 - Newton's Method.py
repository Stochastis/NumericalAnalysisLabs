def f(x):
    return x**2 + 1


def ff(x):
    return 2*x


def Newtons(p0, e, n0):
    i = 1
    p = p0
    while (i <= n0):
        p0 = p
        p = p0 - (f(p0)/ff(p0))
        if abs(p - p0) < e:
            print("Approximation of p: " + str(p))
            print("Approximation of pn-1 " + str(p0))
            print("f(pn) = " + str(f(p0)))
            print("Number of iterations: " + str(i) + "\n")
            return
        i += 1
    print("Failure - Max Iterations Reached")
    print("Approximation of p: " + str(p))
    print("Approximation of pn-1: " + str(p0))
    print("f(pn) = " + str(f(p)) + "\n")


# Test cases
print("Test 1.a\n")
Newtons(0.5, 0.0001, 10)
print("Test 1.b\n")
Newtons(1.4, 0.0001, 8)

while(True):
    p0 = float(input("Please enter your initial guess. "))
    e = float(input("Please enter your desired tolerance. "))
    n0 = int(input("Please enter the maximum number of iterations. "))\

    while (e <= 0):
        e = float(input("Please enter a positive value for tolerance. "))
    while (n0 <= 0):
        n0 = int(input("Please enter a positive number of iterations. "))

    Newtons(p0, e, n0)
