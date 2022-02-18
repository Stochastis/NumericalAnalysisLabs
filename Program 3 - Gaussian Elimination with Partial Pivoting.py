def switchRows(indices, index1, index2):
    temp = indices[index1]
    indices[index1] = index2
    indices[index2] = temp
    return indices


def multiplyAndAdd(matrix, indices, rowToAddTo, rowBeingAdded, scalar):
    scaledRow = [i * scalar for i in matrix[indices[rowBeingAdded]]]
    for i in range(len(matrix[indices[rowToAddTo]])):
        matrix[indices[rowToAddTo]][i] += scaledRow[i]
    print("Added %i * row %i to row %i." % (scalar, rowBeingAdded, rowToAddTo))
    return matrix


def bestFirstRow(matrix, indices, i, n):
    p = 0
    for row in range(n):
        if abs(matrix[indices[row]][i]) > p:
            p = row
    return p


def printMatrix(matrix, indices):
    for index in indices:
        print(matrix[index])
    print('')


def GPP(matrix, indices, n):
    # Elimination Process
    for i in range(n - 1):
        p = bestFirstRow(matrix, indices, i, n)
        if matrix[indices[p]][i] == 0:
            print("No unique solution exists.")
            return
        if p != i:
            indices = switchRows(indices, p, i)
        printMatrix(matrix, indices)
    pass


# Manually enter your data here
matrix = [[1, 6, 3], [4, 5, 6], [7, 0, 9]]
indices = [0, 1, 2]
n = 3
printMatrix(matrix, indices)
GPP(matrix, indices, n)
