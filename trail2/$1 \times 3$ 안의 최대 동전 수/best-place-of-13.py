n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]

max_coins = 0

for i in range(n):
    for j in range(n-2):
        coins = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        max_coins = max(coins,max_coins)

print(max_coins)