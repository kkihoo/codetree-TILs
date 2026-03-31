# 변수 선언 및 입력
n = int(input())

# 숫자로 이루어진 삼각형을 출력합니다.
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(i * j, end=" ")
	print()