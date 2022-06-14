import sys

input = sys.stdin.readline
n = int(input())
number = 1
array = []
result = ""
flag = True
for i in range(n):
    x = int(input())

    while number <= x:
        array.append(number)
        result += "+"

    if array[-1] == x:
        array.pop()
        result += "-"
    else:
        flag = False
        break

if flag == True:  # stack에 원소가 남아있지 않을 때
    for x in result:
        print(x)
else:  # stack에 원소가 남아있을 때
    print("NO")
