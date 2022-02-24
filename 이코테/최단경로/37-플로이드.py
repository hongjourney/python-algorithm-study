"""
# https://www.acmicpc.net/problem/11404
입력 조건
- 첫째 줄에 도시 개수 n, (1<=n<=100)
- 둘째 줄에 버스의 개수 m, (1<=m<=100,000)
- 셋째 줄부터 m+2줄까지 (시작도시, 도착도시, 비용)이 주어짐.
- 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수도 있음. 

출력 조건
- i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는 데 필요한 최소 비용
- 만약 갈 수 없다면 그 자리는 0을 출력
"""
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

import sys
input = sys.stdin.readline
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()
    
"""
- 플로이드 3중 for문에서 i, j, k순으로 짜면 모든 경우의 수 다 고려하지 못함. 
"""

