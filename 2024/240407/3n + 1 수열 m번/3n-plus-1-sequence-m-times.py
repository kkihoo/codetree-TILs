# 변수 선언 및 입력
m = int(input())
	
# m회 반복합니다.
for _ in range(m):
	# 변수 선언 및 입력
	n = int(input())
	ans = 0
		
	# n이 1이 될 때까지 3n + 1을 반복합니다.
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
			
		ans += 1
	
	print(ans)