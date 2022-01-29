"""
입력 조건
    - 첫째 줄에 수의 개수 (2<=n<=11)
    - 둘째 줄에 n개의 수가 주어짐. 
    - 셋째 줄에 합이 n-1인 4개의 정수 주어짐. (+개수, -개수, *개수, /개수)

출력 조건
    - n개 수 사이에 부호를 조합하여 연산한 최대값과 최소값 구하기
    - 연산자 우선순위를 무시하고 앞에서부터 연산
    - 음수를 양수로 나눌 때는 C++14 기준 사용(즉, 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 변환)
    - 최댓값과 최소값은 (-1e9, 1e9) 범위에 존재. 입력값과 중간연산값도 모두 이 범위 내에 존재. 
"""
n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))

min_value, max_value = 1e9, -1e9


def dfs(i, now):
    """
    Args:
        i: 현재 연산하는 숫자의 index (i==n 이면 min_valud, max_value 업데이트)
        now : 이전 단계까지 연산한 결과
    """
    global min_value, max_value, plus, minus, mul, div
    if i == n:
        min_value = min(now, min_value)
        max_value = max(now, max_value)
        return
    if plus > 0:
        plus -= 1  # global 변수
        dfs(i + 1, now + numbers[i])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(i + 1, now - numbers[i])
        minus += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, now * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(now / numbers[i]))
        div += 1


dfs(1, numbers[0])
print(max_value)
print(min_value)

"""
- 종료조건 있는 dfs문제
- 조합, 순열을 dfs/bfs로 푸는 방식. 16-연구소 문제랑 비슷한 듯
- a//b == int(a/b) 인줄 알았는데, a가 음수일 경우 결과가 다를 수 있음. 
- plus -= 1; dfs(); plus += 1 경우의 수 세기. 단 plus는 global 변수 처리
"""
