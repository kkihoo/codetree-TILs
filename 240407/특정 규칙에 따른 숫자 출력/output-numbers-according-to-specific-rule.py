# 변수 선언 및 입력
n = int(input())
cnt = 1;
	
# cnt를 이용해 숫자로 이루어진 삼각형을 출력합니다.
for i in range(n):
	for j in range(i):
		print(" ", end=" ")
	for j in range(n - i):
		print(cnt, end=" ")
		cnt += 1
		if cnt == 10:
			cnt = 1
	print()