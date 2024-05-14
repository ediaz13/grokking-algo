def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

#4.1
def sum_recursive(arr, index):
  if index == len(arr):
    return 0
  else:
    return arr[index] + sum_recursive(arr, index + 1)

#4.2
def count_numbers(arr, index):
  if index == len(arr):
    return 0
  else:
    return 1 + count_numbers(arr, index + 1)

#4.3
def find_highest(arr):
    highest = arr[0]
    highest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index

print(sum([1, 2, 3, 4]))
print(sum_recursive([1, 2, 3, 4], 0))
print(count_numbers([1, 2, 3, 4], 0))