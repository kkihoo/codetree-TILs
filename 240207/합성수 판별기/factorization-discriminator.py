n = int(input())
satis = False
for i in range(2, n+1):
    if n % i == 0:
        satis = True

if satis == True:
    print("C")
else :
    print("N")