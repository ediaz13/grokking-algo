def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def binary_search_recursive(list, item, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if list[mid] == item:
        return mid
    elif list[mid] < item:
        return binary_search_recursive(list, item, mid + 1, high)
    else:
        return binary_search_recursive(list, item, low, mid - 1)

my_List = [1, 3, 5, 7, 9]

print(binary_search(my_List, 3))
print(binary_search(my_List, -1))
print(binary_search_recursive(my_List, 5, 0, len(my_List)))

#Ex 1.1. It would take 7 steps.
#Ex 1.2. It would take 8 steps.


