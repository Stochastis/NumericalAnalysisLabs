def twoPointDerivative(xPoints, yPoints):
    """
    This function approximates the derivative of a function using the two-point formula
    and lagrange interpolating polynomials.
    """

    results = [0, 0]
    h = xPoints[1] - xPoints[0]

    results[0] = (yPoints[1] - yPoints[0]) / h
    results[1] = (yPoints[-1] - yPoints[-2]) / h

    return results


def threePointDerivative(xPoints, yPoints):
    """
    For the second-from-left and second-from-right points,
    the three-point midpoint formula is used."""

    results = [0, 0]
    h = xPoints[1] - xPoints[0]

    results[0] = (yPoints[2] - yPoints[0]) / (2*h)
    results[1] = (yPoints[-1] - yPoints[-3]) / (2*h)

    return


def fivePointDerivative(xPoints, yPoints, pointIndex):
    """
    For all interior points, use the five-point midpoint formula
    using the two closest points on either side."""

    h = xPoints[1] - xPoints[0]
    return


xPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yPoints = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(twoPointDerivative(xPoints, yPoints))
