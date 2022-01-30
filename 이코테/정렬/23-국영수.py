n = int(input())

score = []
for _ in range(n):
    name, kor, eng, math = input().split()
    score.append((int(kor),  int(eng), int(math), name))

score.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for kor, eng, math, name in score:
    print(name)