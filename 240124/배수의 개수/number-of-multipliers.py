cnt = 0
cnt2 = 0
for _ in range(10):
    num = int(input())
    if num % 3 == 0:
        cnt += 1
    if num % 5 == 0:
        cnt2 += 1
print(cnt, cnt2)