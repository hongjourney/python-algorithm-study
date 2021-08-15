x, y, num = map(int, input().split())
total = x+y
result = 0

while total >= num:
    result += total // num
    total = total // num + total % num
    
print(result)