def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    if r*c != m*n:
        return mat
    res = [[0] * c for i in range(r)]
    k = l = 0
    for i in range(r):
        for j in range(c):
            if l == n:
                l = 0
                k += 1
            res[i][j] = mat[k][l]
            l += 1
    return res



print(matrixReshape([[1,2],[3,4]], 1, 4))
print(matrixReshape([[1,2],[3,4]], 2, 2))
