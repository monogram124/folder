nums = [45, 24, -1, 4, 456, 993, -260, 61, 46, 66]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = []
    greater = []

    for num in arr:
        if num == pivot:
            continue

        if num < pivot:
            less.append(num)
        else:
            greater.append(num)
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort(nums))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 19, 20]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

print(binary_search(arr, 21))