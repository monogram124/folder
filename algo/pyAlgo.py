from collections import deque

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# СОРТИРОВКА ПУЗЫРЬКОМ

def bubble_sort(nums):
    for num in range(len(nums) - 1):
        for i in range(len(nums) - 1 - num):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums

# БЫСТРАЯ СОРТИРОВКА

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

# БИНАРНЫЙ ПОИСК

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

# СОРТИРОВКА СЛИЯНИЕМ

def merge_two_lists(a, b):
    i = j = 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    if i < len(a):
        res += a[i:]
    
    if j < len(b):
        res += b[j:]
    
    return res

def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge_two_lists(left, right)

# ПОИСК В ШИРИНУ
def bfs(graph, start):
    queue = deque()
    visited = set()
    queue += graph[start]
    visited.add(start)
    result = []


    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return result

def bfs(graph, start):
    queue = deque()
    visited = set()
    queue += graph[start]
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)