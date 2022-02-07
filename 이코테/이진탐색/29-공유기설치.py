"""
입력 조건
- 집의 개수 n (2<=n<=200,000)와 공유기 개수 c (2<=c<=n)
- 둘째 줄부터 n개의 줄에 집의 좌표 x (1<=x<=1,000,000,000)이 주어짐. 

출력 조건
- 가장 인접한 공유기 사이의 최대 거리 구하기
"""
n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1  # 가능한 최소 거리
end = array[-1] - array[0]  # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    # 가장 인접한 두 공유기 사이의 거리가 mid 일 때.
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # c개 이상의 공유기 설치 가능
        start = mid + 1
        result = mid
    else:  # c개 이상의 공유기 설치 불가능
        end = mid - 1

print(result)
"""
- 공유기 좌표의 최소값과 최댓값을 start, end로 잡고 이진탐색하여 공간을 최대한 분할하고 공간마다 하나씩 뽑으면, '가장 인접한 두 공유기 사이의 거리'를 최대로 만들 수 있을 것이라 생각
- 하지만 분할하고도 전체 공간을 고려해야하므로 이진탐색 방법이 아님. combination과 유사한 효율일 것. 
- 대신 '거리'를 이진탐색 가능. 최소 거리와 최대 거리로 start, end를 잡고
- '가장 인접한 두 공유기 사이의 거리'를 mid로 고정하여 가능한 (c=묶음 개수)를 구하기. c는 2부터 1씩 늘려가며
- 그럼 (거리=gap)과 (묶음 개수=c) 가 가능한지 판단하는 함수를 만들어야하나? 
- 대신 c를 1씩 늘려가며 target_c보다 커지는지 확인할 수 있다.

"""
