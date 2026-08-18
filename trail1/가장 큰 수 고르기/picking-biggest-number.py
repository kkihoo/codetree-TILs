arr = list(map(int,input().split()))

max_val = arr[0]

for i in arr[1:]:
    if i > max_val:
        max_val = i

print(max_val)