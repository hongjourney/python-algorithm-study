from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

if x in array:
    left_index = bisect_left(array, x, x)
    right_index = bisect_right(array, x, x)
    result = right_index-left_index
else:
    result = -1
print(result)

