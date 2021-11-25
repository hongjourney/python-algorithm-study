n, m = map(int, input().split())

max_output = 0
for i in range(n):
    row_lowest = min(map(int, input().split()))
    max_output = max(row_lowest, max_output)

print(max_output)

