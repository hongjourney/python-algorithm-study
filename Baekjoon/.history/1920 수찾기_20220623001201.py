n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))


# def search(num, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if mid == num:
#         return 1
#     elif mid > num:
#         return search(num, start, mid - 1)
#     else:
#         return search(num, mid + 1, end)


# for num in b:
#     start = 1
#     end = a[-1]
#     answer = search(num, start, end)

#     if answer:
#         print(1)
#     else:
#         print(0)


def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    else:
        return search(array, target, mid + 1, end)


for num in b:
    start = 0
    end = n - 1
    index = search(a, num, start, end)

    if index:
        print(1)
    else:
        print(0)
