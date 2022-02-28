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

for i in range(1, n+1):
    array = [0] + list(map(int, input().split())) # 노드 1번~n번
    for j in range(1, n+1):
        if array[j] == 1:
            union(parent, i, j)


target_node = list(map(int, input().split()))
root_node = [find_parent(parent, x) for x in target_node]

result = 'YES'
for node in root_node:
    if node != root_node[0]:
        result = 'NO'
        break
print(result)
    
    