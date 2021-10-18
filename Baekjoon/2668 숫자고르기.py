n = int(input())
numbers = [0]*(n+1)
for i in range(1,n+1):
  numbers[i] = int(input())

result = []

# 한번 탐색할 때마다 start는 고정하고 
# now(현재 방문하는 번호)를 바꿔가며 
# 이미 방문한 경우는 visited[now]=True로 처리
def search(numbers, start, now, visited):
  visited[now] = True
  next_num = numbers[now]

  if not visited[next_num]:
    search(numbers, start, next_num, visited)
  elif visited[next_num] and next_num == start:
    result.append(start)


for i in range(1,n+1):
  visited = [0]*(n+1) 
  search(numbers, i, i, visited)
  

result.sort()
print(len(result))
for num in result:
  print(num)


