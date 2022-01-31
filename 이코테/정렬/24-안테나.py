n = int(input())
location = list(map(int, input().split()))

location.sort()
if n%2!= 0:
    middle_index = int((n-1)/2)
    print(location[middle_index])
else:
    middle_index = int(n/2-1)
    min_value = location[middle_index]
    min_distance = sum([abs(x-location[middle_index]) for x in location])
    for num in range(location[middle_index], location[middle_index+1]):
        distance = sum([abs(x-num) for x in location])
        if distance < min_distance:
            min_value = num
            min_distance = distance
    print(min_value)