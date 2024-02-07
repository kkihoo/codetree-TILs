arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

satis = True

for i in range(a, b + 1):
    if i % c == 0:
        satis = False

if satis == True:
    print("YES")
else:
    print("NO")