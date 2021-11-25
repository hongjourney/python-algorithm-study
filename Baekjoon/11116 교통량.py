n = int(input()) #테스트 케이스 개수
m = []
left_list = []
right_list = []

for i in range(n):
    m.append(int(input()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    left_list.append(left)
    right_list.append(right)

for i in range(m-2)
