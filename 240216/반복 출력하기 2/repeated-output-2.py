def print_hello(N):
    if N == 0:
        return

    print_hello(N-1)
    print("HelloWorld")

N = int(input())
print_hello(N)