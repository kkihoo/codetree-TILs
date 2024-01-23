n = input().split()

a, b = int(n[0]), int(n[1])

i=a
while i <= b:
	print(i, end=" ")
	if i % 2 == 1:
		i *= 2
	else:
		i += 3