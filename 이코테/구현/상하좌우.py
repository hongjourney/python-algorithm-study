"""
입력 조건
- 첫째줄 : n, (1,1)에서 (n,n)까지 정사각형 맵, (1<=n<=100, 정수)
- 둘째줄 : 이동 계획, (R, L, U, D)으로 주어짐 

출력조건
- (1, 1)에서 출발하여 최종 도착 지점 구하기. (n, n) 크기의 정사각형 공간을 벗어나는 움직임은 무시
"""
n = int(input())
map = input().split()

now = [1, 1]
direction = ['R', 'L', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for step in map:
    for i in range(len(direction)):
        if direction[i]==step:
            new_x, new_y = now[0]+dx[i], now[1]+dy[i]
            if new_x in [0, n+1] or new_y in [0, n+1]:
                continue
            now = [new_x, new_y]
            
print(now[0], now[1])