# 문제 링크 : https://www.acmicpc.net/problem/18353


# n = int(input())
# data = [0] + list(map(int, input().split()))

# dp_separate = [0] * (n + 1) # dp_separate[i] : i번째~n번째까지 제외할 수 있는 최소 숫자

# for i in range(n, 0, -1):
#     if i == n:
#         continue
#     if data[i] < data[i + 1]:
#         dp_separate[i] = dp_separate[i + 1] + 1  # i번째를 제외하는 경우
#         for j in range(i + 1, n + 1):
#             if data[i] >= data[j]:
#                 dp_separate[i] = min(dp_separate[i], dp_separate[j] + (j - i))
#     else:
#         dp_separate[i] = dp_separate[i + 1]

# print(dp_separate[1])


"""
내풀이(위)
- 뒤에서부터 i번째까지만 고려했을 때 제외할 수 있는 최소 숫자를 구했음 dp_separate[i]
- 그런데 dp_separate[i]와 dp_separate[i-1]이 경우의 수가 겹침

솔루션(아래)
- i~n번째 중에서만 선택되면서 + i번째는 반드시 포함되는 경우를 계산하기
- 이래야지 중복인 경우의 수를 고려해서 dp 계산을 할 수 있음. 
- dp 초기값은 1, i번째 원소만 포함되는 경우.
"""


n = int(input())
array = list(map(int, input().split()))
# 최소의 인원만 제외하기 => 남는 인원이 최대 => 증가하는 부분 수열 중 최대 길이
array.reverse()

dp = [1] * (n)  # dp[i] : array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
