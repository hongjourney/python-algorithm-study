"""
입력 조건
- 삼각형의 크기 n(1<=n<=500)가 첫째 줄에 주어지고, 둘째 줄부터 n+1 번째 줄까지 정수 삼각형이 주어짐. 
- 정수의 범위는 0이상 9999 이하

출력 조건
- 삼각형의 맨 위층부터 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 떄, 이제까지 선택된 수의 합이 최대가 되는 결과 구하기
- 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능. 
"""
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        left_row, left_col = i - 1, j - 1
        right_row, right_col = i - 1, j
        prev_value = 0
        if left_col >= 0:
            prev_value = max(prev_value, data[left_row][left_col])
        if right_col < i:
            prev_value = max(prev_value, data[right_row][right_col])
        data[i][j] = data[i][j] + prev_value
print(max(data[n - 1]))


"""
# 점화식을 그대로 쓰는 방법은
for i in range(1, n):
    for j in range(i + 1):
        # 왼족 위에서 내려오는 경우
        if j==0:
            left_up = 0
        else:
            left_up = data[i-1][j-1]
        # 오른쪽 위에서 내려오는 경우
        if j==i:
            right_up = 0
        else:
            right_up = data[i-1][j]
        data[i][j] = data[i][j] + max(left_up, right_up) 
"""
