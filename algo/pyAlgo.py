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
    if len(nums) <= 1:
        return nums

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

# АЛГОРИТМЫ ГРАФОВ 
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [7],
    6: [],
    7: []
} 

# ПОИСК В ШИРИНУ
# bfs - алгоритм для нахождения кратчайшего пути меджу двумя веринами в графе
# добавляем в очередь первый элемент, а так же создаем множество для уже посещенных элементов
# пока очерещдь не пуста мы вытаскиваем из нее первый элемент и если он не поосещен делаем следующие проверки:
# если цель возращаем True, если нет добавляем в очередь всех его соседей и опять вытаскиваем первый элемент, пока весь граф не будет пройден
def bfs(start: int, target: int, graph: dict[int]) -> bool:
    queue = deque()
    queue += [start]
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            if node ==  target:
                return True
            
            else:
                queue += graph[node]
                visited.add(node)


    return False

# ПОИСК В ГЛУБИНУ
# dfs - самый базовый алгоритм для прохождения по графу, отличается от dfs тем что ищет не кротчайший а просто путь в графе
# проверяем если наш стартовый узел это цель, и если оне есть в массиве уцже посезенных
# добавляем в массив посещененых, потом проходим по всем его соседям
# если не были в соседе то прохожодим по его соседу, и тд пока не пройдем по всему графу

def dfs(start: int, target: int, graph: dict[int], visited: list[int]) -> bool:
    if start == target:
        return True
    
    if start in visited:
        return False
    
    visited += [start]

    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(neighbour, target, graph, visited):
                return True
            
    return False

# print(dfs(1, 3, graph, []))


# АЛГОРИТМ ДЕЙКСТРЫ
# 