n = int(input())

array = list(map(int, input().split()))


def find_fixed_num(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return find_fixed_num(array, start, mid - 1)
    else:
        return find_fixed_num(array, mid + 1, end)


result = find_fixed_num(array, 0, n - 1)
print(result)
if not result:
    print(-1)
else:
    print(result)
