cnt = 0
while True:
    n =int(input())
    if n % 2 == 0:
        print(n//2)
    elif n % 2 == 1:
        continue
    cnt += 1
    if cnt == 3:
        break