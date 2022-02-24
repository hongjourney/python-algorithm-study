"""
입력 조건
- 첫째 줄에 테스트 케이스 수 t, (1<=t<=10)
- 매 테스트 케이스의 첫째 줄에는 그래프 사이즈인 정수 n이 주어짐. (2<=n<=125)
- 공간은 n*n 크기의 2차원 공간
- 이어서 n개의 줄에 걸쳐 각 칸의 비용이 주어짐. (0<=각 칸의 비용<=9)

출력 조건
- [0][0]위치에서 출발하여 [n-1][n-1] 위치까지 상하좌우로 이동
- 최소 비용으로 이동한 결과를 출력
"""

test_count = int(input())
import heapq

for _ in range(test_count):
    n = int(input())
    INF = int(1e9)
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF]*n for _ in range(n)]
    
    def dijkstra(start_x, start_y):
        q = []
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        distance[start_x][start_y] = graph[start_x][start_y]
        heapq.heappush(q, (distance[start_x][start_y], start_x, start_y))
        while q:
            dist, now_x, now_y = heapq.heappop(q)
            if distance[now_x][now_y] < dist:
                continue
            for i in range(4):
                new_x = now_x + dx[i]
                new_y = now_y + dy[i]
                if new_x < 0 or new_x >=n or new_y <0 or new_y >= n:
                    continue
                cost = dist + graph[new_x][new_y]
                if cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = cost
                    heapq.heappush(q, (cost, new_x, new_y))

    dijkstra(0, 0)
    print(distance[n-1][n-1])

    

    
    

    


    

    
        


     