r, c = map(int, input().split())
grid = [input().split() for _ in range(r)]

ans = 0

for i1 in range(1, r-1):
    for j1 in range(1, c-1):
        for i2 in range(i1 + 1, r - 1):
            for j2 in range(j1 + 1, c - 1):
                if (grid[0][0] != grid[i1][j1] and
                    grid[i1][j1] != grid[i2][j2] and
                    grid[i2][j2] != grid[r - 1][c - 1]):
                    ans += 1
print(ans)