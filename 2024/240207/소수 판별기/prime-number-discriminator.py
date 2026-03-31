n = int(input())

satis = True

i = 2
while i < n :
    if n % i == 0:
        satis = False
        break
    i += 1

if satis == True:
    print("P")
else:
    print("C")