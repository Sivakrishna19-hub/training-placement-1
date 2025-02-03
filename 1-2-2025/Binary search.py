def binary_search(arr, low, high, target):
    if low > high:
        return -1  # Element not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

# Iterative Version
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
print("Recursive Binary Search:", binary_search(arr, 0, len(arr) - 1, target))
print("Iterative Binary Search:", binary_search_iterative(arr, target))
