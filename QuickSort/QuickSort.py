def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sum_recursive(arr, index):
  if index == len(arr):
    return 0
  else:
    return arr[index] + sum_recursive(arr, index + 1)



print(sum([1, 2, 3, 4]))
print(sum_recursive([1, 2, 3, 4], 0))
