def isValidSudoku(board):
    pisya = {i: [] for i in range(0,9)}
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in pisya[i]:
                    return False
                pisya[i].append(board[i][j])
    pisya = {i: [] for i in range(0, 9)}
    for i in range(9):
        for j in range(9):
            if board[j][i] != '.':
                if board[j][i] in pisya[i]:
                    return False
                pisya[i].append(board[j][i])
    pisya[0] = []
    ind = jnd = 3
    while ind <= 9 and jnd <= 9:
        for i in range(ind-3, ind):
            for j in range(jnd-3, jnd):
                if board[i][j] != '.':
                    if board[i][j] in pisya[0]:
                        return False
                    pisya[0].append(board[i][j])
        pisya[0] = []
        ind += 3
        if ind > 9:
            ind = 3
            jnd += 3
    return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([["1","1",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]]))
print(isValidSudoku([[".",".",".",".","5",".",".","1","."],
                     [".","4",".","3",".",".",".",".","."],
                     [".",".",".",".",".","3",".",".","1"],
                     ["8",".",".",".",".",".",".","2","."],
                     [".",".","2",".","7",".",".",".","."],
                     [".","1","5",".",".",".",".",".","."],
                     [".",".",".",".",".","2",".",".","."],
                     [".","2",".","9",".",".",".",".","."],
                     [".",".","4",".",".",".",".",".","."]]))