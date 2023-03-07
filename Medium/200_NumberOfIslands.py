def dfs(grid, i, j, visited):
    visited[i][j] = True
    if j + 1 < len(grid[0]) and grid[i][j + 1] == '1' and not visited[i][j + 1]:
        dfs(grid, i, j + 1, visited)
    if i + 1 < len(grid) and grid[i + 1][j] == '1' and not visited[i + 1][j]:
        dfs(grid, i + 1, j, visited)
    if j - 1 >= 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
        dfs(grid, i, j - 1, visited)
    if i - 1 >= 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
        dfs(grid, i - 1, j, visited)


def numIslands(grid):
    count = 0
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                dfs(grid, i, j, visited)
    return count


print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
