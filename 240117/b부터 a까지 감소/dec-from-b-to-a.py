num = input().split()

a, b = int(num[0]), int(num[1])

for i in range(b, a-1, -1):
    print(i, end = ' ')