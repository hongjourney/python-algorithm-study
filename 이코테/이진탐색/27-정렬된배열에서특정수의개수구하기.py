n, x = map(int, input().split())
array = list(map(int, input().split()))

#### bisect 라이브러리 이용했던 코드
# from bisect import bisect_left, bisect_right
# if x in array:
#     left_index = bisect_left(array, x, x)
#     right_index = bisect_right(array, x, x)
#     result = right_index-left_index
# else:
#     result = -1
# print(result)

#### 이진탐색 구현한 코드
start = 0
end = len(array)
target_index = -1
while start<end:
    mid = (start+end)//2
    if array[mid] == x:
        target_index = mid
        break
    elif array[mid] < x:
        start = mid + 1
    else:
        end = mid - 1

if target_index != -1:
    left_index, right_index = target_index, target_index
    while array[right_index] == x:
        right_index += 1
    while array[left_index] == x:
        left_index -= 1
    print(right_index-left_index-1) 
else:
    print(-1)

"""[solution]

# array에 target 원소가 없을 때 -1 처리하는 건 count_by_value 바깥으로 뺌. 함수에는 하나의 목적만. 
# 가장 왼쪽 인덱와 가장 오른쪽 인덱스를 각각 이진 탐색함. 

def count_by_value(array, x):
    n = len(array)
    left_index = first(array, x, 0, n-1)
    if left_index == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환
         
    right_index = last(array, x, 0, n-1)

    return right_index-left_index+1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return
    mid = (start + end)//2
    # 가장 왼쪽 인덱스인 경우에만 인덱스 반환
    if (mid==0 or array[mid-1] < target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        first(array, target, mid+1, end)
    else:
        first(array, target, start, mid-1)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return
    mid = (start + end)//2
    # 가장 오른쪽 인덱스인 경우에만 인덱스 반환
    if (mid==end or array[mid+1] > target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        last(array, target, mid+1, end)
    else:
        last(array, target, start, mid-1)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)

"""

