# 변수 선언 및 입력
n = int(input())
	
# 숫자로 이루어진 삼각형을 출력합니다.
for i in range(n, 0, -1):
	for j in range(n, 0, -1):
		if j > i:
			print(" ", end=" ")
		else:
			print(j, end=" ")
	print()