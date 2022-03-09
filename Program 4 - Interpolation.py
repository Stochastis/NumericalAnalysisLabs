import math


def NewtonDDFCoefficients(xPoints, yPoints):
    n = len(xPoints)-1
    f = [[0]*(n+1)for i in range(n+1)]

    for i in range(n+1):
        f[i][0] = yPoints[i]

    # Error checking
    if len(xPoints) != len(yPoints):
        print("Error: Number of x and y values do not match.")
        return

    for i in range(1, n+1):
        for j in (range(1, i+1)):
            f[i][j] = (f[i][j-1] - f[i-1][j-1]) / (xPoints[i] - xPoints[i-j])

    printF(f)
    print("")

    result = [0]*(n+1)
    for i in range(n+1):
        result[i] = f[i][i]
    return result


def printF(F):
    for row in F:
        print(row)


def newtonDDFEstimate(xPoint, coefficients, xPoints):
    factor = 1
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * factor
        factor *= (xPoint - xPoints[i])
    return "P(%f) = %f" % (xPoint, result)


def NCS(x, a):
    n = len(x) - 1

    # Initialize h
    h = [0]*n
    for i in range(n - 1):
        h[i] = x[i+1] - x[i]

    # Compute b-vector
    alpha = [0]*(n-1)
    for i in range(1, n - 1):
        alpha[i] = (3 / h[i])(a[i+1] - a[i]) - (3 / h[i-1])(a[i] - a[i-1])

    # Begin solving - solving c_0 using LU-decomposition
    l, mu, z = [0]*(n-1)
    l[0] = 1

    # solving c_i
    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - (h[i-1] * mu[i-1])
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - (h[i-1] * z[i-1])) / l[i]

    # solving c_n
    l[n] = 1
    z[n] = 0
    b, c, d = [0]*n

    # Back-Substitution and the remaining substitutions


# Test 1.a (NewtonDDF)
# print("Test 1.a: \n")
# xPoints = [0, 1, 2, 3]
# yPoints = [1, math.e, math.e**2, math.e**3]
# coefficients = NewtonDDFCoefficients(xPoints, yPoints)
# print("Coefficients: " + str(coefficients) + "\n")
# print(newtonDDFEstimate(1.5, coefficients, xPoints) + "\n----------------------\n")

# # Test 1.b (NewtonDDF)
# print("Test 1.b: \n")
# xPoints = [1.0, 1.3, 1.6, 1.9, 2.2]
# yPoints = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
# coefficients = NewtonDDFCoefficients(xPoints, yPoints)
# print("Coefficients: " + str(coefficients) + "\n")
# print(newtonDDFEstimate(1.5, coefficients, xPoints) + "\n----------------------\n")

# # Test 2.a (Natural Cubic Spline)
