arr = input().split()
c = str(arr[0])
n = int(arr[1])

if c == "A" or "D":
    for i in range(1, n+1):
        print(i, end = ' ')