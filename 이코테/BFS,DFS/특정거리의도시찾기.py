
"""
입력 조건
- 도시 개수 (2<=n<=300,000), 도로 개수 (1<=m<=1,000,000), 거리 정보 (1<=k<=300,000), 출발 도시 정보 (1<=x<=n)
- (a,b): a번 도시에서 b번 도시로 이동하는 단방향 도로 존재. (1<=a,b<=n)
- a -> b 거리는 1, x번-> x번 거리는 0

출력 조건
- x로부터 출발하여 도달할 수 있는 도시 중, 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
- 존재하지 않는다면 -1 출력
    
"""
n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)] # 인접 노드 리스트
visited = [0]*(n+1) # 노드별 방문 여부
distance = [0]*(n+1) # 노드별 최단 거리

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

from collections import deque

def bfs(start, visited, graph, distance):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                distance[i] = distance[x] + 1
                visited[i] = True

    return distance

distance = bfs(x, visited, graph, distance)

answer = [i for i, number in enumerate(distance) if number==k]

if not answer:
    print(-1)
else:
    print(sorted(answer))


"""
개선사항
- visited 대신 노드별 최단거리distance를 -1으로 초기화하고, distance[i]가 -1인지 확인해서 방문 여부 확인 가능
- 번호가 이미 오름차순이므로 sorted 안 해도 됨
- x와 i를 now, next_node 등으로 변수명 바꾸는게 이해하기 좋을듯
"""
