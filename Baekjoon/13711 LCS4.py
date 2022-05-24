import bisect
import sys

input = sys.stdin.readline
n = int(input())
seq_a = list(map(int, input().split()))
seq_b = list(map(int, input().split()))

new_a = [] # seq_a를 seq_b의 인덱스로 표현하기

for i in range(n):
    x = seq_b.index(seq_a[i])
    new_a.append(x)


# new_a 가장 긴 증가하는 부분 수열 (longest increasing subsequence) 찾기

dp = [new_a[0]] # 정렬 가정

for i in range(1, n):
    if new_a[i] > dp[-1]: # max(dp)보다 큰 경우 
        dp.append(new_a[i])
    else: # max(dp)보다 작은 경우
        idx = bisect.bisect_left(dp, new_a[i])
        dp[idx] = new_a[i] # 더 작은 수로 대체

print(len(dp)) 



"""
# 시간복잡도 O(N**2), N*N 크기의 배열 만들어야함. N의 최대 10만이므로 메모리 초과
# 1) seq_b의 인덱스 기준으로 seq_a를 표현한 새로운 수열 new_a를 구하고 
# 2) new_a의 LIS를 구하는 문제와 seq_a와 seq_b의 LCS 문제는 동일한 문제가 됨. 
# 만약 1부터 N까지 모든 수가 한번씩 등장한다는 조건이 없다면? 1)이 불가능함. 
array = [[0]*(n+1) for _ in range(n+1)] # array[i][j] = seq_a[:i]와 seq_b[:j]의 공통 부분 수열의 최대 길이

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==0 or j==0:
            array[i][j] = 0
        elif seq_a[i-1]==seq_b[j-1]:
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = max(array[i-1][j], array[i][j-1])

print(array[n][n])
"""