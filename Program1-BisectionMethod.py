import math

def f(x):
    # Change this return command to your desired function
    return ((x**2) - 1)

def g(x):
    return (math.exp(1)**(1 - (x**2)))

def bisection(a, b, e, n):
    i = 1
    fa = f(a)
    
    while (i <= n):
        p = a + ((b-a)/2)
        fp = f(p)

        if (fp == g(p) or ((b-a)/2) < e):
            print("f(p) = " + str(fp))
            print("Number of iterations required to terminate: " + str(i))
            return p

        i += 1

        if ((fa > g(a) and fp < g(p)) or (fa < g(a) and fp > g(p))):
            b = p
        else:
            a = p
            fa = fp

    print("Failure - Max Iterations Reached")
    return

while (True):
    a = float(input("Enter a value for a. "))
    b = float(input("Enter a value for b. "))
    while (a == b):
        print("Please make sure that a and b are different.")
        a = float(input("Enter a value for a. "))
        b = float(input("Enter a value for b. "))

    e = float(input("Enter a value for the tolerance. "))
    while (e <= 0):
        e = float(input("Please enter a positive value for the tolerance. "))

    n = int(input("Enter a max number of iterations. "))
    while (n <= 0):
        int(input("Please enter a positive value for the maximum number of iterations. "))
    print("Estimated p = " + str(bisection(a, b, e, n)))
