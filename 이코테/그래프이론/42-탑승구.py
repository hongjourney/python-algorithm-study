from collections import deque
g = int(input())
p = int(input())

parent = [0]*(g+1)
queue = deque()
for _ in range(p):
    queue.append(int(input()))

for i in range(1, p+1):
    x = queue.popleft()
    if parent[x] < x :
        for j in range(x, g+1):
            parent[j] += 1
    elif parent[x] == x:
        result = i-1 # 마지막으로 도킹한 비행기 수
        break
print(result)

"""
- 서로소 집합 알고리즘으로 해결 가능
- 각 노드(1번~g번 탑승구 + 0번 탑승구도 추가)를 서로 다른 집합이라 생각, 처음은 모두 루트 노드로 자기 자신을 가리킴
- 도킹에 성공하면 해당 집합을 바로 왼쪽 집합과 합한다. 단, 집합의 루트가 0이면 더이상 도킹 불가능
- 임의의 x에 대해 x번 노드(탑승구)의 부모노드는 x번 이하 노드 중 도킹 가능한 수. x번 노드에 도킹한다면 parent[x] 는 parent[x-1]이 됨. 
"""
"""
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
parent = [0]*(g+1)
for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) 
    if data == 0:
        break
    union(parent, data, data-1)
    result += 1
print(result)

"""