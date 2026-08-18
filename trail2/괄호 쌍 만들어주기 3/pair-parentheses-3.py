a = str(input().split())

ans = 0

for i in range(len(a)):
    if a[i] == "(":
        for j in range(i+1, len(a)):
            if a[j] == ")":
                ans += 1

print(ans)