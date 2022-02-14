"""
입력 조건
- n번째 못생긴 수, (1<=n<=1000)

출력 조건
- 2,3,5 만을 소인수로 가지는 수를 못생긴 수라고 한다. 그리고 1은 못생긴 수라고 가정
- n번째 못생긴 수를 출력
"""

n = int(input())

result = []
result.append(1) 
ugly = [2,3,5]
now = ugly
result+= now

while len(result) <= n:
    temp = []
    for i in ugly:
        temp += [x*i for x in now]
    now = list(set(temp))
    result += now
    result.sort()

print(result[n-1])


"""
- 2, 3, 5를 차례대로 곱하고 set을 통과한 뒤 더한 후 정렬하는 코드를 짰는데 n이 클수록 정렬에서 효율성이 떨어진다.
- 아래 솔루션처럼 1부터 n까지 next2, next3, next5를 구하기. next2 = 2를 소인수로 가지는 다음 못생긴 수
- next2 = 2*(이전 못생긴 수)
- (이전 못생긴 수)= ugly[index] 에서 index는 소인수마다 1씩 올려간다. (i2, i3, i5)

### 솔루션(이코테)
ugly = [0]*n # 못생긴 수를 담기 위한 테이블(1차원 DP 테이블)
ugly[0] = 1 

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0 

# 처음에 곱셈값을 초기화
next2, next3, next5 = 2,3,5

# 1부터 n까지의 못생긴 수 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2]*2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3]*3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5]*5 
"""