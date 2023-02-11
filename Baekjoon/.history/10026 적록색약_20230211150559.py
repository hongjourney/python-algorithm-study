""""""
n = 5
grid = [
    ["R", "R", "R", "B", "B"],
    ["G", "G", "B", "B", "B"],
    ["B", "B", "B", "R", "R"],
    ["B", "B", "R", "R", "R"],
    ["R", "R", "R", "R", "R"],
]
""""""
# n = int(input())
visited = [[0] * n for _ in range(n)]  # (0: 방문전 1: B방문, 2: R또는 B방문)

# grid = []
# for _ in range(n):
#     grid.append(list(input().split()))

count = [0, 0]  # [적록색약 아닌 사람 시선, 적록색약 사람 시선]


def dfs(x, y, grid, visited, target):
    if x < 0 or y < 0 or x >= n or y >= n:
        return None
    if visited[x][y] == 0 and grid[x][y] == target:  # 방문 전
        if target in ["R", "G"]:
            visited[x][y] = 2
        else:
            visited[x][y] = 1
        dfs(x + 1, y, grid, visited, target)
        dfs(x - 1, y, grid, visited, target)
        dfs(x, y + 1, grid, visited, target)
        dfs(x, y - 1, grid, visited, target)
        return True
    return None


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            color = grid[i][j]
            if dfs(i, j, grid, visited, color):
                count[0] += 1  # 적록색약 아닌 사람 시선
new_visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if new_visited[i][j] == 0:
            target = visited[i][j]  # 1 또는 2
            if dfs(i, j, visited, new_visited, target):
                count[1] += 1

print(count, end=" ")
