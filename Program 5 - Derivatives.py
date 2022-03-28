def twoPointDerivative(xPoints, yPoints):
    """
    This function approximates the derivative of a function using the two-point formula
    and lagrange interpolating polynomials.
    """

    twoPoints = []
    h = xPoints[1] - xPoints[0]

    twoPoints[0] = (yPoints[1] - yPoints[0]) / h

    return twoPoints


xPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yPoints = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
