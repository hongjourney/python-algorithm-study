"""
입력 조건
- 지도 크기 nxn (1<=n<=200), 바이러스 종류 k가지(1<=k<=1000)
- n개 줄에 걸쳐 바이러스 번호 주어짐. 모든 바이러스의 번호는 k이하의 자연수, 바이러스 없으면 0
- s, x, y : s초 뒤에 (x,y) 위치에 존재하는 바이러스(0<=s<=10,000)(1<=x,y<=n)

출력 조건
- 모든 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식. 매초 번호가 낮은 종류부터 먼저 증식함. 
- 이미 특정 칸에 어떤 바이러스 존재한다면 다른 바이러스가 증식 불가능
- s초 뒤에 (x, y)위치에 존재하는 바이러스 종류를 출력. 바이러스가 존재하지 않는다면 0출력
"""

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


s, x, y = map(int, input().split())

from collections import deque

queue = deque()


def find_virus(virus_number):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == virus_number:
                queue.append((virus_number, i, j))


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

time = 0  # 0초
for virus_number in range(1, k + 1):
    find_virus(virus_number)

while time < s:
    for _ in range(len(queue)):
        virus_number, now_x, now_y = queue.popleft()
        for direction in range(4):
            new_x, new_y = now_x + dx[direction], now_y + dy[direction]
            if (
                new_x >= 0
                and new_x < n
                and new_y >= 0
                and new_y < n
                and graph[new_x][new_y] == 0
            ):
                graph[new_x][new_y] = virus_number
                queue.append((virus_number, new_x, new_y))
    time += 1


print(graph[x - 1][y - 1])

"""
내 코드
- find_virus : 초기 바이러스 위치를 큐에 넣음(-> 대신 graph에 입력할 때 큐에 넣어도 됐을 듯)
- 매 초마다 큐에 있는 모든 자료를 꺼냈음. 매 초마다 큐의 길이만큼 for문 작성(-> 대신 큐에 time 정보도 넣었다면, time==s일때 종료되는 while queue를 쓸 수 있었을 것)
"""
