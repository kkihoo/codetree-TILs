# n = int(input())

# for i in range(n*2):
#     if i % 2 == 0:
#         for _ in range(int(1 + (i / 2))):
#             print("*", end = " ")
#         print()
#     if i % 2 == 1:
#         for _ in range(int(n - (i - 1) / 2)):
#             print("*", end = " ")
#         print()

n = int(input())

for i in range(1, n + 1):
    for _ in range(i):
        print("* ", end="")
    print()
    for _ in range(n - i + 1):
        print("* ", end="")
    print()