# 변수 선언 및 입력
n = int(input())
	
# 특이한 조건대로 구구단을 출력합니다.
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if (i + j) % 4 == 0:
			print(f"({i}, {j})")
		else:
			print(f"({i}, {j})", end=" ")