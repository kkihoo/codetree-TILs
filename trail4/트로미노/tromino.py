n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

for i in range(n-1):
    for j in range(m-1):
        block = [
            grid[i][j], grid[i][j+1],
            grid[i+1][j], grid[i+1][j+1]
        ]
        max_sum = max(max_sum, sum(block)- min(block))

for i in range(n):
    for j in range(m - 2):
        total = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_sum = max(max_sum, total)

for i in range(n-2):
    for j in range(m):
        total = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        max_sum = max(max_sum, total)

print(max_sum)