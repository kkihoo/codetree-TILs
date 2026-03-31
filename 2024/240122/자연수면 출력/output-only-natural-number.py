n = input().split()

a, b = int(n[0]), int(n[1])

if a > 0 :
    for i in range(b):
        print(a, end = '')
if a <= 0:
    print(0)