n, m = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0

for r in range(n):
    for c in range(n):
        for k in range(2 * n + 1):
            gold_count = 0

            for i in range(n):
                for j in range(n):
                    if abs(r - i) + abs(c - j) <= k:
                        if grid[i][j] == 1:
                            gold_count += 1


            cost = k * k + (k + 1) * (k + 1)
            if gold_count * m >= cost:
                max_gold = max(max_gold, gold_count)

print(max_gold)