def f(x):
    return x


def ff(x):
    return x

def Newtons(p0,e,n0):
    i = 1
    while (i <= n0):
        p = p0 - f(p0)/ff(p0)
        if abs(p - p0) < e:
            return p
        i += 1
        p0 = p
    print("Failure - Max Iterations Reached")
    return

p0 = float(input("Please enter your initial guess."))
e = float(input("Please enter your desired tolerance."))
n0 = int(input("Please enter the maximum number of iterations."))\

while (e <= 0):
    e = float(input("Please enter a positive value for tolerance."))
while (n0 <= 0):
    n0 = int(input("Please enter a positive number of iterations."))