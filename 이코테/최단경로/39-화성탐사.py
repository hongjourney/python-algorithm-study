test_count = int(input())
import heapq

for _ in range(test_count):
    n = int(input())
    INF = int(1e9)
    graph = []
    distance = [[INF]*n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
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

    

    
    

    


    

    
        


     