def generate(numRows):
    res = [[1] * i for i in range(1, numRows + 1)]
    for i in range(2, numRows):
        for j in range(1, len(res[i]) - 1):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

    return res


print(generate(5))
