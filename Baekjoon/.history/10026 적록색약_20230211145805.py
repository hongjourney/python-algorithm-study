n = int(input())
visited = [[0] * n for _ in range(n)]  # (0: 방문전 1: B방문, 2: R또는 B방문)

grid = []
for _ in range(n):
    grid.append(list(input().split()))

count = [0, 0]  # [적록색약 사람 시선, 적록색약 아닌 사람 시선]


def dfs(x, y, grid, target):
    if x < 0 or y < 0 or x >= n or y >= n:
        return None
    if visited[x][y] == 0 and grid[x][y] == target:  # 방문 전
        if target in ["R", "G"]:
            visited[x][y] = 2
        else:
            visited[x][y] = 1
        dfs(x + 1, y, grid, target)
        dfs(x - 1, y, grid, target)
        dfs(x, y + 1, grid, target)
        dfs(x, y - 1, grid, target)
        return True
    return None


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            color = grid[i][j]
            if dfs(i, j, grid, color):
                count[1] += 1  # 적록색약 아닌 사람 시선
new_visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            target = visited[i][j]  # 1 또는 2
            if dfs(i, j, visited, target):
                count[0] += 1

print(count)
