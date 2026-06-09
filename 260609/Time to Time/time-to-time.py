a, b, c, d = map(int, input().split())

# Please write your code here.
hour, mins = a, b
times = 0

while True:
    if hour == c and mins == d:
        break

    times += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(times)