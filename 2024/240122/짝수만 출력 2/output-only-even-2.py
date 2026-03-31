n = input().split()
b = int(n[1])
a = int(n[0])

while a >= b:
    if a % 2 == 0:
        print(a, end = ' ')
    a -= 1