import math
m, n = map(int, input().split())

array = [True]*(n+1)
array[1] = False # 1은 소수가 아님

for i in range(2, int(math.sqrt(n))+1): 
    if array[i] == True: # i가 소수인 경우만 
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i]:
        print(i)
        
'''
# 빠트린 것
# 1. 2부터 n의 제곱근까지 확인
# 2. 현재 가장 작은 소수 i에 대해서 확인
for i in range(2, n+1):
    j = 2
    while i*j <= n:
        array[i*j] = False
        j += 1

for i in range(m, n+1):
    if array[i]:
        print(i)
'''