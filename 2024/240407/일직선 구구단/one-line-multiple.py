# 변수 선언 및 입력
n = int(input())
	
# 일직선으로 구구단을 출력합니다.
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(f"{i} * {j} = {i * j}")