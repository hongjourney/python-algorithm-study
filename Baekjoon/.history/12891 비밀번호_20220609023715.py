s, p = map(int, input().split())
words = input()

array = list(map(int, input().split()))  # acgt
condition_dict = {}
dna = ["A", "C", "G", "T"]

for x in dna:
    condition_dict[x] = 0

for i in range(len(dna)):
    condition_dict[dna[i]] += array[i]

# 부분 문자열 : 문자열의 연속된 일부
temp = {}
for x in dna:
    temp[x] = 0

result = 0

for i in range(s - p + 1):
    valid = True
    if i == 0:
        for j in range(p):
            temp[words[j]] += 1
            if temp[words[j]] > condition_dict[words[j]]:
                valid = False

    else:
        before_word = words[i - 1]
        now_word = words[i + p - 1]
        temp[before_word] -= 1
        temp[now_word] += 1
        for key, value in temp.items():
            if value > condition_dict[key]:
                valid = False
                break

    if valid == True:
        result += 1
        

print(result)