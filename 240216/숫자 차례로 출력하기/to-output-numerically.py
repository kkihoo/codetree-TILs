def num1(N):
    if N == 0:
        return
    num1(N-1)    
    print(N, end = " ")


def num2(N):
    if N == 0:
        return

    print(N, end = " ") 
    num2(N-1)    



N = int(input())
num1(N)
print()
num2(N)