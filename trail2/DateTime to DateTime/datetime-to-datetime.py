a, b, c = map(int, input().split())

# Please write your code here.
day, hour, mins = 11, 11, 11
elapsed_times = 0

if (a, b, c) < (11, 11, 11):
    print("-1")
else:
    while True:
        if day == a and hour == b and mins == c:
            break

        mins += 1
        elapsed_times += 1

        if mins == 60:
            hour += 1
            mins = 0
        if hour == 24:
            day += 1
            hour = 0
    print(elapsed_times)