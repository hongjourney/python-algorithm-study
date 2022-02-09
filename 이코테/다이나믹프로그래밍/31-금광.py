"""
입력 조건
- 테스트케이스 t (1<=t<=1000)
- 매 테스트케이스 첫째줄에 n, m (1<=n,m<=20), 둘째 줄에 nxm 개의 위치에 매장된 금의 개수(1이상 100이하)가 입력됨.

출력 조건
- 채굴자는 첫 번째 열부터 출발하여 열을 한칸씩 움직여가면서 금을 캔다. 맨 처음은 어느 행에서든 출발 가능. 
- 매번 오른쪽 위, 오른쪽, 오른쪽 아래 중 하나의 위치로 이동 가능
- 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 구하라.
"""
t = int(input())

size = []
data = []
import numpy as np

for _ in range(t):
    n, m = map(int, input().split())
    size.append([n, m])
    array = list(map(int, input().split()))
    array = np.reshape(array, (n, m))
    data.append(array)

row = [-1, 0, 1]
col = [1, 1, 1]

for i in range(t):
    n, m = size[i]
    array = data[i]

    for j in range(1, m):
        for k in range(n):
            max_result = 0
            for direction in range(3):
                past_row = k - row[direction]
                past_col = j - col[direction]

                if past_row >= 0 and past_row < n:
                    max_result = max(
                        max_result, array[past_row][past_col] + array[k][j]
                    )
            array[k][j] = max_result

print(max([x[m - 1] for x in array]))

"""
# 솔루션
# 왼쪽 위, 왼쪽 아래, 왼쪽에서 오는 경우를 명시해서 인덱스 벗어나는 경우는 0으로 예외 처리함. 
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 2차원 dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽위에서 오는 경우
            if i == 0: # 현재 row
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래서 오는 경우
            if i == n-1: # 현재 row
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)
"""
