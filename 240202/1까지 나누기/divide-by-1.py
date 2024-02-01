n = int(input())
cnt = 0

for i in range(1,5001):
    cnt += 1
    n = n // i
    if n <= 1:
        break

print(cnt)