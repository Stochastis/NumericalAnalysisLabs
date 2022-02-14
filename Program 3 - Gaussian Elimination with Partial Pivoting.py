def switchRows(indices, index1, index2):
    temp = index1
    indices[index1] = index2
    indices[index2] = temp
    print("Switched rows " + str(index1) + " and " + str(index2) + ".")
    return indices


def multiplyAndAdd(matrix, indices, rowToAddTo, rowBeingAdded, scalar):
    scaledRow = [i * scalar for i in matrix[indices[rowBeingAdded]]]
    for i in range(len(matrix[indices[rowToAddTo]])):
        matrix[indices[rowToAddTo]][i] += scaledRow[i]
    print("Added %i * row %i to row %i." % (scalar, rowBeingAdded, rowToAddTo))
    return matrix


def bestFirstRow(matrix, indices):
    pass


def printMatrix(matrix, indices):
    for index in indices:
        print(matrix[index])
    print('')


def GPP(matrix, indices, n):
    # Elimination Process
    for i in range(n - 1):

        pass
    pass


# Manually enter your data here
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
indices = [0, 1, 2]
n = 3
