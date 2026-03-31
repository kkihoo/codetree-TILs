n = int(input())
sum_val = 0
cnt = 0
for _ in range(n):
    a = int(input())
    sum_val += a
    cnt += 1
avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")