n, m = map(int,input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    max_streak = 1
    current_streak = 1

    for j in range(1,n):
        if grid[i][j] == grid[i][j-1]:
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)

    if max_streak >= m:
        cnt += 1

for j in range(n):
    max_streak = 1
    current_streak = 1

    for i in range(1,n):
        if grid[i][j] == grid[i-1][j]:
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)
    
    if max_streak >= m:
        cnt += 1

print(cnt)