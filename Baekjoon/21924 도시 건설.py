import sys
input = sys.stdin.readline

# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합집합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a >= b :
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split()) # 건물개수, 도로개수

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i # 자기 자신으로 부모노드 초기화

info = []
result = 0 # 모든 비용
for i in range(m):
    a, b, dist = map(int, input().split())
    info.append((dist, a, b))
    result += dist

# 비용을 기준으로 정렬
info.sort()

for x in info:
    dist, a, b = x
    if find_parent(parent, a) == find_parent(parent,b):
        continue
    else:
        union_parent(parent, a, b)
        result -= dist
check = [find_parent(parent,x) for x in parent[1:]]
if len(set(check)) == 1:
    print(result)
else:
    print(-1)

