from collections import Counter
from collections import deque

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
        
        # print(len(vals), sum(vals))
        
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


def isPalindrome(s: str) -> bool:
    s = s.lower()
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in s:
        if char not in a:
            s = s.replace(char, '')

    if s == s[::-1]:
        return True
    else:
        return False
    
# print(isPalindrome("A man, a plan, a canal: Panama"))

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    res = [0 for num in range(0, len(nums))]

    where = 0

    i = 0
    j = -1

    while i != len(nums):
        if j >= len(nums) - 1:
            i += 1
            j = -1
            where += 1

        if nums[j] < nums[i]:
            res[where] += 1
            j += 1
        else:
            j += 1

        if i == len(nums) - 1 and j == len(nums) - 1:
            break

    return res

# print(smallerNumbersThanCurrent([8,1,2,2,3]))

x = "привет"

print(type(x))

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    name_height = {}

    for i in range(0, len(names)):
        name_height[heights[i]] = names[i]

    sorted_heights = sorted(name_height.keys(), reverse=True)
    print(sorted_heights)
    res = []

    for height in sorted_heights:
        res.append(name_height[height])

    return res

# print(sortPeople(["Mary","John","Emma"], [180,165,170]))

def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    count = 0

    i = 0
    j = 0

    while i <= len(arr1) - 1:
        if j == len(arr2):
            j = 0
            i += 1

        # print(arr1[i], arr2[j])


        if abs(arr1[i] - arr2[j]) <= d:
            count += 1
            j += 1
        else:
            j += 1

        if i == len(arr1) - 1 and j == len(arr2) - 1:
            break
    
    return count

# print(findTheDistanceValue([4,5,8], [10,9,1,8], 2))

def binary(nodes):
    res = 0
    n = len(nodes) - 1

    for i in range(0, len(nodes)):
        res += (nodes[i] * 2**(n-i))

    return res
print(binary([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]))

    