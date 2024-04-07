# 변수 선언 및 입력
n = int(input())
cnt = 1

# 숫자로 이루어진 삼각형을 출력합니다.
for i in range(n):
	for _ in range(i + 1):
		print(cnt, end=" ")
		cnt += 1
	print()