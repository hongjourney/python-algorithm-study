"""
입력 조건
- 지도 크기 (nxm), (3<=n, m<=8)
- n개 줄에 걸쳐 지도 모양 입력됨. 0은 안전 영역, 1은 벽, 2는 바이러스 있는 위치 (2<=바이러스 위치 개수<10), (3<=안전 영역 개수)

출력 조건
- 바이러스는 상하좌우 인접한 안전 영역으로 모두 퍼질 수 있다. 벽으로는 퍼질 수 없음. 
- 벽을 3개 더 세워 바이러스가 퍼지는 것을 막으려고 할 때
- 얻을 수 있는 최대 안전 영역 크기를 출력

"""
n, m = map(int, input().split())
graph = []
temp_graph = [[0] * m for _ in range(n)]  # 바이러스가 퍼지는 것을 가정한 임시 지도

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]  # 아래, 왼, 위, 우
dy = [0, -1, 0, 1]

result = 0  # 0의 최대 개수


def spread_virus(now_x, now_y):
    for i in range(4):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]

        if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m:
            if temp_graph[new_x][new_y] == 0:
                temp_graph[new_x][new_y] = 2
                spread_virus(new_x, new_y)


def dfs(count):
    """
    벽을 세울 수 있는 모든 경우의 수 고려. 
    벽의 개수(count)를 1개씩 늘려가고, 3개가 되면 spread_virus를 실행시켜 result(안전 영역 크기) 구함. 
    """
    # count : 벽 개수
    global result  # 최소값 확인을 위해 dfs함수 인자로 들어가는 대신 global
    if count == 3:  # 종료 조건, result 값 확인
        for i in range(n):
            for j in range(m):
                temp_graph[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 2:
                    spread_virus(i, j)
        zero_count = 0
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 0:
                    zero_count += 1
        result = max(result, zero_count)
        return  # 벽 3개 설치 했으므로 끝

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽세우기
                count += 1
                dfs(count)
                graph[i][j] = 0  # 벽없애기
                count -= 1


dfs(0)
print(result)

"""
생각할 점
- temp_graph(리스트)는 global 처리 안 해도 수정 가능하다. 왜?
    - mutable(ex. list, dict, set) 과 immutable(ex. string, bool, int, float, tuple) 차이
    - mutable은 indexing, slicing 등으로 값 변경 가능(새로운 객체 생성하는 재할당 하지 않고)
    - 함수에 파라미터로 mutable 객체를 넘기면, local 변수와 global 변수가 동일한 객체를 가리킴
    - (but, mutable을 재할당하려면 global 써야함.)
- dfs의 마지막 이중 for문이 어떻게 3개 벽을 세우는 모든 경우의 수를 탐색한다고 보장하나?
    - 처음에는 모든 조합을 고려해야하니 itertools.combinations를 생각했는데 dfs를 이용할 수도 있구나
    - 종료 조건은 count=3 일 때
    - 벽을 순차적으로 세우고 있고, 이중 for문으로 모든 경우의 수를 고려함. 
    - 때문에 이미 확인했던 경우를 중복으로 고려할 수 있을 듯 (중복되는 경우의 수 ex. [[1,2],[2,1],[2,2]] 위치에 벽을 세우기와 [[2,1],[1,2],[2,2]] 위치에 벽을 세우기)
- 지금은 n,m이 최대 8이라 시간 초과가 안 될 수 있지만 지도 크기가 커질 수록 이 방식이 비효율적일듯. 개선할 수는 없을까
"""

