def switchRows(indices, index1, index2):
    temp = indices[index1]
    indices[index1] = indices[index2]
    indices[index2] = temp
    print("Switched rows %i and %i." % (index1, index2))
    printMatrix(matrix, indices)
    return indices


def multiplyAndSubtract(matrix, indices, subtractFrom, subtracted, scalar):
    scaledRow = [i * scalar for i in matrix[indices[subtracted]]]
    for i in range(len(matrix[indices[subtractFrom]])):
        matrix[indices[subtractFrom]][i] -= scaledRow[i]
    print("Subtracted (%f * row %i) from row %i." %
          (scalar, subtracted, subtractFrom))
    printMatrix(matrix, indices)
    return matrix


def bestFirstRow(matrix, indices, i, n):
    p = i
    for row in range(i, n):
        if abs(matrix[indices[row]][i]) > matrix[indices[p]][i]:
            p = row
    return p


def printMatrix(matrix, indices):
    for index in indices:
        print(matrix[index])
    print('')


def GPP(matrix):
    n = len(matrix)
    indices = [0]*n
    for i in range(n):
        indices[i] = i
    printMatrix(matrix, indices)
    # Make all entries a float for display purposes
    for row in range(n):
        for column in range(n+1):
            matrix[indices[row]][column] *= 1.0
    solutions = [0]*(n)
    # Elimination Process
    for i in range(n - 1):
        p = bestFirstRow(matrix, indices, i, n)
        if matrix[indices[p]][i] == 0:
            print("No unique solution exists.")
            return
        # Pivot rows
        if p != i:
            indices = switchRows(indices, p, i)
        for j in range(i+1, n):
            m = matrix[indices[j]][i] / matrix[indices[i]][i]
            multiplyAndSubtract(matrix, indices, j, i, m)
    if matrix[indices[-1]][-2] == 0:
        print("No unique solution exists.")
        return
    # Xn = right side of equation divided by coefficient
    solutions[-1] = matrix[indices[-1]][-1] / matrix[indices[-1]][-2]
    for i in range(n-1, 0, -1):
        sum = 0
        for j in range(i, n):
            sum += matrix[indices[i-1]][j] * solutions[j]
        solutions[i-1] = (matrix[indices[i-1]][-1] - sum) / \
            matrix[indices[i-1]][i-1]
    return solutions


# Manual Test:
print('Manual Test:\n------------')
# Enter your augmented matrix below
matrix = [[1, -0.25, 0, -0.25, 0, 0, 0, 0, 0, 90/4],
          [-0.25, 1, -0.25, 0, -0.25, 0, 0, 0, 0, 90/4],
          [0, -0.25, 1, 0, 0, -0.25, 0, 0, 0, 90/4],
          [-0.25, 0, 0, 1, -0.25, 0, -0.25, 0, 0, 0],
          [0, -0.25, 0, -0.25, 1, -0.25, 0, -0.25, 0, 0],
          [0, 0, -0.25, 0, -0.25, 1, 0, 0, -0.25, 0],
          [0, 0, 0, -0.25, 0, 0, 1, -0.25, 0, 90/4],
          [0, 0, 0, 0, -0.25, 0, -0.25, 1, -0.25, 90/4],
          [0, 0, 0, 0, 0, -0.25, 0, -0.25, 1, 90/4]]
print('Solution: %s' % (str(GPP(matrix))))
