satis = True

for i in range(5):
    n = int(input())
    if n % 3 != 0 :
        satis = False
        break

if satis == True:
    print("1")
else:
    print("0")