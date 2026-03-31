cnt = 0
sum_val = 0
while True :
    n = float(input())
    if n >= 30 or n < 20:
        break
    else : 
        sum_val += n
        cnt += 1
print(f"{(sum_val/cnt):.2f}")