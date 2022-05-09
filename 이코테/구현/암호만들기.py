from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
array = list(input().split())
array.sort()

for password in combinations(array, l):
    count = 0 # 모음 개수
    for i in password:
        if i in vowels:
            count += 1
    
    if count > 0 and count < l-1:
        print(''.join(password))


'''
# 두 번 sort하는 대신, 입력 받을 때부터 sort 하면 한 번에 가능.
l, c = map(int, input().split())
letters = list(input().split())

import itertools

result = []
for group in itertools.combinations(letters, l):
    vowels_count = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    for letter in list(group):
        if letter in vowels_list:
            vowels_count += 1
    if vowels_count == 0 or vowels_count >= l-1:
        continue
    result.append(''.join(sorted(list(group))))

result.sort()
for x in result:
    print(x)
'''
