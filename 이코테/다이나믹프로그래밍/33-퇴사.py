"""
https://www.acmicpc.net/problem/14501
입력 조건
- 첫째 줄에 전체 상담 개수 n (1<=n<=15)
- 둘째 줄부터 n개 줄까지 기간 t과 금액 p가 구분되어서 주어짐. (1일<=t<=5일, 1<=p<=1000)

출력 조건
- 1일부터 n일까지, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하라. 
"""
n = int(input())
plan = [[]]
for _ in range(n):
    plan.append(list(map(int, input().split())))

# 뒤에서부터
dp = [0] * (n + 1)  # dp[i] : i일을 선택했을 때 받을 수 있는 최대 금액
for i in range(n, 0, -1):
    max_value = 0
    for j in range(i, n + 1):
        t, p = plan[j]
        if j + t - 1 > n:  # n+1 일째 이후
            continue
        if j + t - 1 == n:  # n일째
            max_value = max(max_value, p)
        else:  # n일째 이하
            max_value = max(max_value, p + dp[j + t])
    dp[i] = max_value

print(max(dp))

"""
- i일 이후부터의 최대 금액을 계산하기 위해 i부터 n까지 for문을 만들었지만 그렇게 하지 않아도 max_value에 계속해서 저장하면 된다. (솔루션처럼)
- 그럼 뒤쪽 날짜부터 앞쪽 날짜까지 max_value는 단조증가하는 형태
"""

""" 
# solution
n = int(input()) # 전체 상담 개수
t = [] # 상담하는데 걸리는 시간
p = [] # 상담했을 때 받을 수 있는 금액
dp = [0]*(n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0 # 뒤쪽 날짜부터 max_value 계산

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점회식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
print(max_value)
"""

