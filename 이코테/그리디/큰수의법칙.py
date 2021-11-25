n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
mul = m//(k+1) # numbers[0]+numbers[1] 세트가 곱해지는 개수
remain = m%(k+1)

result = (numbers[0]*k+numbers[1])*mul + numbers[0]*remain
print(result)

# 반복되는 수열로 생각하여 numbers[0]가 더해지는 횟수, numbers[1]가 더해지는 횟수를 각각 생각해도 됨. 