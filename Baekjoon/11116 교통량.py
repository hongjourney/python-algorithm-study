"""
일정 간격으로 떨어져있는 두 줄
예를 들어 자동차가 왼쪽에서 오른쪽으로 갈 때, 두 줄을 지나면서
[왼쪽 줄 시작, 왼쪽 줄 끝, 오른쪽 줄 시작, 오른쪽 줄 끝] = [t, t+500, t+1000, t+1500]
와 같은 기록을 남긴다. (500간격)

입력조건
- 첫째줄 : 테스트 케이스 개수, n(1<=n<=100)
- 각각의 테스트 케이스에 대해 
    - 첫째줄 : 측정된 시간 기록 개수, m(m<=200)
    - 둘째줄, 셋째줄 : 차례대로 왼쪽 기록 m개, 오른쪽 기록 m개 (시간기록은 10^9이하)
- ex)  
2
4
17 517 1432 1932
432 932 1017 1517
6
235 451 735 951 2351 2851
1235 1351 1451 1735 1851 1951

출력조건
- 왼쪽에서 오는 차의 숫자
- ex)
1
2

"""
n = int(input()) #테스트 케이스 개수
m = []
left = []
right = []
for i in range(n):
    m.append(int(input()))
    left.extend(list(map(int, input().split())))
    right.extend(list(map(int, input().split())))

