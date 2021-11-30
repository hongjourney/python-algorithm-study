"""
입력조건
- 첫째줄 : n (0<=n<=23, 정수)

출력조건
- 00시00분00초~ n시59분59초까지 3이 하나라도 포함되는 시각의 경우의 수
"""
n = int(input())

# n=0 일때 경우의 수
# 3, 13, 23, 30~39, 43, 53 (총 15개)
count = 15*60 + 60*15 - 15*15

if n < 3:
    result = count*(n+1)
elif n < 13:
    result = count*n + 1*60*60
elif n < 23:
    result = count*(n-1) + 2*60*60
else:
    result = count*(n-2) + 3*60*60

print(result)
