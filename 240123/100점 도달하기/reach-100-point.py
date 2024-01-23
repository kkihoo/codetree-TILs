n = int(input())

for i in range(n,101):
    if i < 60:
        print("F", end = ' ')
    elif 70 > i >= 60:
        print("D", end = ' ')
    elif 80 > i >= 70:
        print("C", end = ' ')
    elif 90 > i >= 80:
        print("B", end = ' ')
    else:
        print("A", end = ' ')