def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
location = [[]]

for i in range(1, n+1):
    location.append(list(map(int, input().split())))

edges = []

for i in range(1, n+1):
    for j in range(i, n+1):
        ax, ay, az = location[i]
        bx, by, bz = location[j]

        dist = min(abs(ax-bx), abs(ay-by), abs(az-bz))
        edges.append((dist, i, j))

edges.sort()

parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

result = 0

for i in range(len(edges)):
    dist, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += dist

print(result)