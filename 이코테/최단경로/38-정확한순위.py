"""
입력 조건
- 첫째 줄에 학생 수 n, (2<=n<=500)
- 둘째 줄에 학생 수 m, (2<=m<=10,000)
- 다음 m개의 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 a, b가 주어짐. (a가 b보다 낮다는 것을 뜻함)

출력 조건
- 성적 순위를 정확히 알 수 있는 학생이 몇 명인지
"""
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


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
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

"""
- 성적 낮은 학생이 높은 학생을 가리키는 방향 그래프로 표현 가능. 방향 그래프 형태로 표현하면 최단 경로 계산하는 문제로 볼 수 있다.
- A에서 B로 도달이 가능하거나 B에서 A로 도달이 가능하면 성적 비교가 가능
- 반대로 A에서 B로 도달이 불가능하고 B에서 A로 도달이 불가능하다면 성적 비교 결과를 알 수 없음. 
- 그래서 n개의 모든 노드에 대해 다른 노드와 서로 도달이 가능한지 확인. 
- 만약 모든 노드와 서로 도달 가능한 상태라면 정확한 순위를 알 수 있음을 의미

# result 구하는 부분 수정
result = 0 
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)


"""