def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid 
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
        
    return None

list = [1, 2, 3, 4, 5, 6]
print(binary_search(list, 2))
print(binary_search(list, 6))
print(binary_search(list, -1))