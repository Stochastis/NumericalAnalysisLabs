def switchRows(indices, index1, index2):
    temp = indices[index1]
    indices[index1] = indices[index2]
    indices[index2] = temp
    print("Switched rows %i and %i." % (index1, index2))
    printMatrix(matrix, indices)
    return indices


def multiplyAndAdd(matrix, indices, rowToAddTo, rowBeingAdded, scalar):
    scaledRow = [i * scalar for i in matrix[indices[rowBeingAdded]]]
    for i in range(len(matrix[indices[rowToAddTo]])):
        matrix[indices[rowToAddTo]][i] -= scaledRow[i]
    print("Added %f * row %i to row %i." % (scalar, rowBeingAdded, rowToAddTo))
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


def GPP(matrix, indices, n):
    solutions = [0]*(n-1)
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
            multiplyAndAdd(matrix, indices, j, i, m)
    if matrix[indices[n-1]][n-1] == 0:
        print("No unique solution exists.")
        return
    # Xn = right side of equation divided by coefficient
    solutions[-1] = matrix[indices[-1]][-1] / matrix[indices[-1]][-2]
    for i in range(n-1, 0, -1):
        sum = 0
        for j in range(i+1, n):
            sum += matrix[indices[i]][j] * solutions[j]
        solutions[i] = (matrix[indices[-1]][i] - sum) / matrix[indices[i]][i]
    return solutions


# Manually enter your data here
# Augmented matrix
matrix = [[1, 1, 1, 3], [1, 2, 3, 0], [1, 3, 2, 3]]

n = len(matrix)
indices = [0]*n
for i in range(n):
    indices[i] = i
printMatrix(matrix, indices)
print(GPP(matrix, indices, n))
