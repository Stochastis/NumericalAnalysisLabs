import math


def NewtonDDF(xPoints, yPoints):
    n = len(xPoints)-1
    F = [[0]*(n+1)]*(n+1)
    printF(F)

    F[0] = yPoints
    printF(F)

    # Error checking
    if len(xPoints) != len(yPoints):
        print("Error: Number of x and y values do not match.")
        return

    for i in range(1, n+1):
        for j in (range(1, i+1)):
            F[i][j] = (F[i][j-1] - F[i-1][j-1]) / (xPoints[i] - xPoints[i-j])

    result = [0]*(n+1)
    for i in range(n+1):
        result[i] = F[i][i]
    return result


def printF(F):
    for row in F:
        print(row)


xPoints = [0, 1, 2, 3]
yPoints = [1, math.e, math.e**2, math.e**3]

print(NewtonDDF(xPoints, yPoints))
