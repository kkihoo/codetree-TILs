arr = input().split()
a, b = int(arr[0]), int(arr[1])

satis = False

for i in range(a, b + 1):
    if 1920 % i == 0 or 2880 % i == 0:
        satis = True

if satis == True:
    print(1)
else:
    print(0)