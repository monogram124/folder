from collections import Counter
from collections import deque
# def merge_two_lists(a, b):
#     i = j = 0
#     c = []

#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
        
#     if i < len(a):
#         c.append(a[i:])

#     if j < len(b):
#         c.append(b[j:])

#     return c

# def merge_sort(nums):
#     if len(nums) == 1:
#         return nums
    
#     mid = len(nums) // 2

#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])

#     return merge_two_lists(left, right)

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (right+left) // 2

#         if target == arr[mid]:
#             return True
#         elif target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
        
#     return False

# print(binary_search(merge_sort([-1, -2, 123, 7, 14, 153, 75, 9]), 123))

# def bubble_sort(nums):
#     for i in range(len(nums) - 1):
#         for num in range(len(nums) - i - 1):
#             if nums[num] > nums[num+1]:
#                 nums[num], nums[num+1] = nums[num+1], nums[num]

#     return nums

# # print(bubble_sort([-1, -2, 123, 7, 14, 153, 75, 9]))

# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
 
#     less = []
#     greater = []
#     pivot = nums[len(nums) // 2]

#     for num in nums:
#         if num == pivot:
#             continue
     
#         if num < pivot:
#             less.append(num)
#         else:
#             greater.append(num)

#     return quick_sort(less) + [pivot] + quick_sort(greater)

# # print(quick_sort([-1, -2, 123, 7, 14, 153, 75, 9]))

# def bfs(start: int, target: int, graph: dict[int]) -> bool:
#     queue = deque()
#     queue += [start]
#     visited = set()

#     while queue:
#         node = queue.popleft()

#         if node not in visited:
#             if node == target:
#                 return True
#             else:
#                 queue += graph[node]
#                 visited.add(node)

#     return False

# def dfs(start: int, target: int, graph: dict[int], visited: list[int]) -> bool:
#     if start == target:
#         return True
#     elif start in visited:
#         return False
    
#     visited += [start]

#     for n in graph[start]:
#         if n not in visited:
#             if dfs(n, target, graph, visited):
#                 return True
    
#     return False



# LEETCODE PROBLEMS


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

def task1(nums1, nums2):
    big = nums1 + nums2
          
    counter = {}
    res = []
        
    for num in big:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1
        
    for key, val in counter.items():
        if val >= 2 and key in nums1 and key in nums2:
            res.append(key)
        
    return res

# print(task1(nums1, nums2))


def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True

    for x in range(1, n):
        if n == 3**x:
            return True
        
    return False
        
# print(isPowerOfThree(59048))

def missingNumber(nums) -> int:
    nums = sorted(nums)
    ran = range(0, len(nums) + 1)
    

    # print(list(ran))
    # print(nums)

    i = j = 0
    
    while i < len(nums) and j < len(list(ran)):
        if nums[i] == ran[j]:
            i += 1
            j += 1
        else:
            return ran[j]
        
    if j == len(nums):
        return ran[len(ran) - 1]

# print(missingNumber([0,1]))


def targetIndices(nums, target) -> list[int]:
    dic = {}
    res = []

    nums = sorted(nums)

    for num in range(0, len(nums)):
        dic[num] = nums[num]
    
    print(dic)

    for key, val in dic.items():
        if val == target:
            res.append(key)
    
    return res

# print(targetIndices([1, 2, 5, 2, 3], 2))

def maxFrequencyElements(nums: list[int]) -> int:
        counter = Counter(nums)
        
        vals = sorted(counter.values())
        
        print(len(vals), sum(vals))
        
        # if len(vals) == sum(vals):
        #     return sum(vals)
        
        # print(max(vals)) # первая строчка

        left = 0
        right = len(vals) - 1
        res = 0

        while left <= right:
           
            mid = (left + right) // 2
            
            # print(vals[mid]) # вторая и третья
            
            if vals[mid] == max(vals):
                res += vals[mid]
            if vals[mid] > max(vals):
                right = mid - 1
            else:
                left = mid + 1

        return res

# print(maxFrequencyElements([6,13,15,15,11,6,7,12,4,11])) # четвертая

def getSum(a, b):
    return sum(a, b)

print(getSum(1, 2))