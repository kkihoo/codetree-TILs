# 변수 선언 및 입력
n = int(input())

# n회 반복합니다.
for _ in range(n):
	# 변수 선언 및 입력
	inp = input()
	arr = inp.split()
	a = int(arr[0])
	b = int(arr[1])
	ans = 1
		
	# a부터 b까지 전부 곱한 값을 출력합니다.
	for i in range(a, b + 1):
		ans *= i
		
	print(ans)