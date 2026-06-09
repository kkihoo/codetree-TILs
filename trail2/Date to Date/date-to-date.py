m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month, day = m1, d1
elapsed_days = 1

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    if month == m2 and day == d2:
        break

    elapsed_days += 1
    day += 1

    if day > days_in_month[month]:
        month += 1
        day = 1

print(elapsed_days)