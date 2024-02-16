N = int(input())

def func(N):
    if N == 0:
        return

    print(N, end = " ")
    func(N - 1)
    print(N, end = " ")

func(N)