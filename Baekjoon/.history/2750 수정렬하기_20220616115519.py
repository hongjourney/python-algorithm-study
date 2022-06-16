n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
    l = len(array)
    if l > 1:
        for i in range(l - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]

for number in array:
    print(number)

