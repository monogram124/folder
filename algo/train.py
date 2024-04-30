def merge_two_lists(a, b):
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
        
    if j < len(b):
        c += b[j:]

    return c

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge_two_lists(left, right)

print(merge_sort([-1, -2, 123, 7, 14, 153, 75, 9]))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right+left) // 2

        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
        
    return False

print(binary_search(merge_sort([-1, -2, 123, 7, 14, 153, 75, 9]), 123))

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for num in range(len(nums) - i - 1):
            if nums[num] > nums[num+1]:
                nums[num], nums[num+1] = nums[num+1], nums[num]

    return nums

print(bubble_sort([-1, -2, 123, 7, 14, 153, 75, 9]))

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
 
    less = []
    greater = []
    pivot = nums[len(nums) // 2]

    for num in nums:
        if num == pivot:
            continue
     
        if num < pivot:
            less.append(num)
        else:
            greater.append(num)

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([-1, -2, 123, 7, 14, 153, 75, 9]))