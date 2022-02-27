"""
입력조건
- n개 노드 (2<=n<=20000), m개 간선 (1<=m<=50000)
- 이후 m개 줄에 걸쳐서 서로 연결된 두 노드 a, b의 번호가 입력됨
- 노드 간 최소 거리는 지나는 간선의 최소 개수

출력 조건
- 1번 노드에서 출발하여 각 노드까지의 최소 거리를 계산하고 
- 가장 멀리 있는 노드와 그 노드까지의 거리, 동일한 거리만큼 떨어져 있는 노드 개수를 출력
- 만약 거리가 같은 노드가 여러 개면 가장 작은 노드 번호를 출력
"""
import heapq
n, m = map(int, input().split())
INF = int(1e9)
graph = [[0]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


start = 1
q = []
heapq.heappush(q, (0,start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue
    for new in graph[now]:
        cost = dist + 1
        if cost < distance[new]:
            distance[new] = cost
            heapq.heappush(q, (cost, new))
max_distance = max(distance[1:])
same_distance_count = 0
max_distance_node = 0
for i in range(1, n+1):
    if distance[i] == max(distance):
        if max_distance_node == 0:
            max_distance_node = i
        same_distance_count += 1
print(max_distance_node, max_distance, same_distance_count)

"""
- 거리가 1이기 때문에 bfs를 이용할 수도 있으나 다익스트라 알고리즘을 이용함. 
"""
        



