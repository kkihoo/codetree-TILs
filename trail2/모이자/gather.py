import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize

for i in range(n):
    total = 0

    for j in range(n):
        total += abs(i-j)*arr[j]

    min_dist = min(min_dist, total)

print(min_dist)

