n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
    l = len(array)
    if l > 1:
        for i in range(l - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]

for number in array:
    print(number)

"""
# 정렬 라이브러리 시간복잡도 O(NlogN)로 풀수도 있음
# 삽입정렬의 시간복잡도 O(N^2), 하지만 거의 정렬되어있을 때는 O(N)으로 빠름. 
"""

