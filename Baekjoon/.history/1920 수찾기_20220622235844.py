n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))
b.sort()


def search(num, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if mid == num:
        return 1
    elif mid > num:
        return search(num, start, mid - 1)
    else:
        return search(num, mid + 1, end)


start = 1
end = a[-1]

for num in b:
    answer = search(num, start, end)

    if answer:
        print(1)
    else:
        print(0)
    start = num

