def f(x):
    # Change this return command to your desired function
    return (x**3 - (9*x))


def bisection():
    a = float(input("Enter a value for a."))
    b = float(input("Enter a value for b."))
    while (a == b):
        print("Please make sure that a and b are different.")
        a = float(input("Enter a value for a."))
        b = float(input("Enter a value for b."))
    fa = f(a)
    fb = f(b)
    if (fa * fb > 0):
        print("Not possible to guarantee a solution.")
        return

    e = float(input("Enter a value for the tolerance."))
    while (e <= 0):
        e = float(input("Please enter a positive value for the tolerance."))

    n = int(input("Enter a max number of iterations."))
    while (n <= 0):
        int(input("Please enter a positive value for the maximum number of iterations."))

    i = 1

    while (i <= n):
        p = a + ((b-a)/2)
        fp = f(p)

        if (fp == 0 or ((b-a)/2) < e):
            print("f(p) = " + str(fp))
            print("Number of iterations required to terminate: " + str(i))
            return p

        i += 1

        if (fa * fp > 0):
            a = p
            fa = fp
        else:
            b = p

    print("Failure - Max Iterations Reached")
    return


while (True):
    print("Estimated p = " + str(bisection()))
