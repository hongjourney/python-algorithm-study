a = input()
b = input()


# 삭제하고 삽입이 연달아 일어나면 replace로 합칠 수 있음 .
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
dp[0] = list(range(len(b)+1))
for i in range(1,len(a)+1):
    dp[i][0] = i
a = '.'+a
b = '.'+b
for i in range(1,len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 # 삭제, 삽입, 교체

print(dp[len(a)-1][len(b)-1])

"""
# 처음 시도
- 5001로 a와 b의 동일한 문자열을 만들고 교집합의 문자에 인덱스를 차례대로 기록하려함. 예) a=cat, b=cut 이면 a = [0,5001,1], b=[0,5001,1]
- 그런데 알파벳이 중복인 단어의 경우 애매해짐 
- 솔루션 참고하여 2차원 dp 테이블 생성

# 솔루션
- dp[x][y] = a[:x+1]에서 b[:y+1] 로 변경될 때 최소 편집 거리
- dp[x-1][y], dp[x][y-1], dp[x-1][y-1] 을 알면 dp[x][y]를 알 수 있다.
- a[x]==b[y]이면 dp[x][y] = dp[x-1][y-1]
- a[x]!=b[y]이면 dp[x][y]는 dp[x-1][y] + 1(삽입) or dp[x][y-1] + 1(삭제) or dp[x-1][y-1] +1 (교체) 중 최소값. 


def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    dp = [[m]+1 for _ in range(n+1)]

    # dp 테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i 
    for j in range(1, m+1):
        dp[0][j] = j
    
    for i in range(1,n+1):
        for j in range(1, m+1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면, 3가지 경우 중에서 최소값 찾기
            else:                   
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]
    
"""

