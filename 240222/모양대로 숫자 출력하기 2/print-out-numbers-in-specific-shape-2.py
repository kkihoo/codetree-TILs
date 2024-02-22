n = int(input())

cnt = 2
for i in range(n):
    for j in range(n):
        print(cnt, end =' ')
        cnt += 2
        if cnt > 9:
            cnt = 2
    print()