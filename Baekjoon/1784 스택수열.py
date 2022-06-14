import sys

input = sys.stdin.readline
n = int(input())
target_array = []
for _ in range(n):
    target_array.append(int(input()))
result = ""
array = []  # stack

number = 1  # 1부터 n까지의 정수 중 하나
target_array_index = 0  # 원하는 수열의 인덱스

while target_array_index <= n - 1:
    # push
    while number <= target_array[target_array_index]:
        array.append(number)
        result += "+"
        number += 1

    # pop
    last = array[-1]
    if target_array[target_array_index] != last:  # 이걸 안 하면 시간초과
        break
    while target_array[target_array_index] == last:
        array.pop()
        result += "-"
        target_array_index += 1

        if not array:
            break
        last = array[-1]

if not array:  # stack에 원소가 남아있지 않을 때
    for x in result:
        print(x)
else:  # stack에 원소가 남아있을 때
    print("NO")


"""
# target_array를 만들지 않고도
# 수 하나씩 입력 받을 때마다 push or pop 수행해도 됨.
number = 1
array = []
result = ""
flag = True
for i in range(n):
    x = int(input())

    while number <= x:
        array.append(number)
        result += "+"
        number += 1

    if array[-1] == x:
        array.pop()
        result += "-"
    else:
        flag = False
        break
"""
