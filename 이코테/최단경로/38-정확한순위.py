n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    lower, higher = map(int, input().split())
    graph[lower][higher] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0

for i in range(1, n+1):
    lower_list = graph[i][1:]
    higher_list = [x[i] for x in graph[1:]]
    assert len(lower_list)==len(higher_list)
    
    lower_count = len([x for x in lower_list if x<INF and x!=0])
    higher_count = len([x for x in higher_list if x<INF and x!=0])
    if lower_count+higher_count+1 == n:
        result += 1
print(result)

