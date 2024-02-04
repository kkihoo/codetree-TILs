while True :
    n = input().split()

    a, b, c = int(n[0]), int(n[1]), str(n[2])
    print(a * b)
    if c == "C":
        break