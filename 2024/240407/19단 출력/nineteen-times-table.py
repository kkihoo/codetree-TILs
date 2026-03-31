n = 19

for first in range(1, n + 1):
    for second in range(1, n + 1):
        if second % 2 == 1:
            # Case 1:
            print(first, "*", second, "=", first * second, end="")
        else:
            # Case 2:
            print(" /", first, "*", second, "=", first * second)
        
        if second == 19:
            # Case 3:
            print()