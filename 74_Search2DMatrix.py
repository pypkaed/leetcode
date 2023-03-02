def searchMatrix(matrix, target):
    for i in range(0, len(matrix) - 1):
        if matrix[i][0] <= target < matrix[i + 1][0]:
            for j in range(0, len(matrix[0])):
                if target == matrix[i][j]:
                    return True
    for j in range(0, len(matrix[0])):
        if target == matrix[len(matrix) - 1][j]:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]], 30))
print(searchMatrix([[1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]], -1))
print(searchMatrix([[1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]], 62))
print(searchMatrix([[1]], 1))
