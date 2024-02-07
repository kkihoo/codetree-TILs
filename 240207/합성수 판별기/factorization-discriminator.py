n = int(input())

for i in range(2, n+1):
    if n % i == 0:
        satis = True
    else :
        satis = False
if satis == True:
    print("C")
else :
    print("N")