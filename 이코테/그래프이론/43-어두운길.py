n, m = map(int, input().split())

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

parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

import heapq
q = []
price = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(q, (z, x, y))
    price += z

use = 0
while q:
    dist, a, b = heapq.heappop(q)
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        use += dist

print(price-use)