'''
n이 1이 될 때까지 (n에서 1을 빼기 or n을 k로 나누기) 과정 횟수의 최소값 구하는 문제
"n이 k의 배수가 될 때까지 1씩 빼고, n이 k의 배수이면 k로 나누기"가 항상 정답인 이유?
- k가 2이상이면, 1을 뺐을 때보다 k로 나눴을 때 훨씬 더 빨리 감소하고
- n이 클수록 k로 나눴을 때 더 많이 감소한다. 
- 그래서 k가 2 이상이기만 하면, k로 나누는 것이 1을 빼는 것보다 항상 빠르게 n의 값을 줄일 수 있다.  
'''
n, k = map(int, input().split())
result = 0

while n > 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result += 1

print(result)
