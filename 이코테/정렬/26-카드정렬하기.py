"""
입력 조건
- 정렬된 카드 묶음 개수 N (1<=N<=100,000)
- N개줄에 걸쳐 카드 묶음의 크기가 입력됨. 

출력 조건
- 정렬된 두 묶음의 카드가 있을 때 각 묶음의 카드의 수를 A, B라고 하면 보통 두 묶음을 합쳐서 하나로 만드는 데이는 A+B번의 비교를 해야함.
- N개의 카드 묶음 크기가 주어질 때, 모두 합치려면 최소한 몇 번의 비교가 필요한지 출력. 
"""

# n = int(input())
# cards = []
# for _ in range(n):
#     cards.append(int(input()))

# result = 0
# cards.sort()
# while len(cards) > 1:
#     new = sum(cards[:2]) # 가장 작은 두 횟수 합치기
#     result += new
#     cards = [x for x in cards[2:] if x <= new] + [new] + [x for x in cards[2:] if x > new]

# print(result)

import heapq
n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    result += one+two
    heapq.heappush(heap, one+two)

print(result)


"""
- 처음에 위쪽 코드로 제출했다가 시간 초과.
- 솔루션 참고) 우선순위 큐를 이용하면 push, pop할 때마다 정렬된 결과를 얻을 수 있음. 파이썬 heapq 라이브러리 이용. 
"""