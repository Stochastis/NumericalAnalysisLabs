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


def threePointEndpointDerivative(xPoints, yPoints):
    """
    Three-point endpoint formula is used.
    """

    h = xPoints[1] - xPoints[0]

    result = ((-3)*yPoints[0] + 4*yPoints[1] - yPoints[2]) / (2*h)

    return result


def threePointMidpointDerivative(xPoints, yPoints):
    """
    For the second-from-left and second-from-right points,
    the three-point midpoint formula is used.
    """

    results = [0, 0]
    h = xPoints[1] - xPoints[0]

    results[0] = (yPoints[2] - yPoints[0]) / (2*h)
    results[1] = (yPoints[-1] - yPoints[-3]) / (2*h)

    return results


def fivePointDerivative(xPoints, yPoints, pointIndex):
    """
    For all interior points, use the five-point midpoint formula
    using the two closest points on either side."""

    h = xPoints[1] - xPoints[0]
    return (yPoints[pointIndex - 2] - 8*yPoints[pointIndex - 1] + 8*yPoints[pointIndex + 1] - yPoints[pointIndex + 2]) / (12*h)


xPoints = [0, 5, 10]
yPoints = [0, 383, 742]
print(threePointEndpointDerivative(xPoints, yPoints))
