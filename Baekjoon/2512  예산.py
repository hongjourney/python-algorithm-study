"""
# 런타임 에러 
n = int(input())
request = list(map(int, input().split()))  # n개 예산
budget = int(input())  # 총 예산


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(n):
            if i <= mid:
                total += array[i]
            else:
                total += array[mid]

        if total == target:
            return array[mid], mid
        elif total < target:
            start = mid + 1
        else:
            end = mid - 1
    return array[end], end


# 예산 모두 배정 가능
if sum(request) <= budget:
    result = max(request)

# 예산 초과
else:
    request.sort()
    limit, limit_index = binary_search(request, budget, 0, n - 1)
    sum_below_limit = sum(request[: limit_index + 1])
    while True:
        limit += 1
        if sum_below_limit + limit * (n - limit_index - 1) <= budget:
            result = limit
        else:
            break

print(result)
"""

# 0부터 100,000 탐색으로 변경

n = int(input())
request = list(map(int, input().split()))  # n개 예산
budget = int(input())  # 총 예산

# 예산 모두 배정 가능
if sum(request) <= budget:
    print(max(request))

# 예산 초과
else:
    start, end = 0, 100000
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in request:
            if x <= mid:
                total += x
            else:
                total += mid
        if total > budget:
            end = mid - 1
        else:
            start = mid + 1
    print(end)

