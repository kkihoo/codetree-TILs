N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_coins = 0

for i in range(N-2):
    for j in range(N-2):
        coins = 0
        for k in range(3):
            for l in range(3):
                coins += grid[i+k][j+l]

        max_coins = max(max_coins, coins)
print(max_coins)