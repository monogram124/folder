# связный список

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        newNode = Node(val)

        if not self.head or not self.tail:
            self.head, self.tail = newNode, newNode

            return
    
        self.tail.next = newNode
        self.tail = newNode

    def print(self):
        nodes = []

        curNode = self.head

        while curNode:
            nodes.append(curNode.val)
            curNode = curNode.next

        return nodes
    
    def prepend(self, val):
        newNode = Node(val, self.head)

        newNode = self.head

        if not self.tail:
            self.tail = newNode

    def find(self, val):
        if not self.head:
            return None
        
        curNode = self.head

        while curNode:
            if curNode.val == val:
                return curNode
            
            curNode = curNode.next
        
        return None
    
    def len(self):
        curNode = self.head
        counter = 0  

        while curNode:
            counter += 1
            curNode = curNode.next

        return counter
    
    def max(self):
        maxNode = 0
        curNode = self.head
    
        while curNode:
            if curNode.val > maxNode:
                maxNode = curNode

            curNode = curNode.next

        return maxNode
    
    def min(self):
        minNode = float("inf")
        curNode = self.head

        while curNode:
            if curNode.val < minNode:
                minNode = curNode
            
            curNode = curNode.next

        return minNode
    
    # def remove(self, val):


    def insert(self, val, prev):
        if not prev:
            return None
        
        newNode = Node(val)

        newNode.next = prev.next
        prev.next = newNode

        if newNode.next == None:
            self.tail = newNode


list = LinkedList()
list.append(8)
list.append(9)
list.insert(12, list.find(8))
list.append(3)

print(list.print())
print(list.find(9))

from collections import deque

# ГРАФЫ
# алгоритм поиска в ширину (Breadth-First Search BFS) - алгоритм дающий ответ на вопрос "Каклй кротчайший путь ведет к X?"

# граф - структура данных, моделирующая набор связей между объектами
# вершины лежащие через одно ребро называются соседними

# ПОИСК В ШИРИНУ, отвечает на вопросы:
# - есть ли путь из вершины A к вершине B?
# - как выглядит кротчайший путь из A к B?

# существуют связи 1, 2 и тд уровней, связи меньшиз уровней предпочтительнее чем больших, это значит что мы не должны проходиться по 2 например когда не закончили 1
# и для операций такого рода, чтобы понимать кто за следует за кем, существует структура данных очередь:

# ОЧЕРЕДЬ работает точно так же как и в реальной жизни, кто ближе к входу тот и первый, в очереди как и в стеке вы не можете обращаться к произвольным элементам
# Принцип работы очереди: FIFO(First in First Out) Принцип работы стека: LIFO(Last in First Out), именно принцип FIFO очереди можно оиспользовать для реализации списка элементов для обхода в графе

# РЕАЛИЗАЦИЯ ГРАФА
test_graph = {
    "me": ["bob", "alex", "steve"],
    "steve": ["bob"],
    "bob": [],
    "alex": []
} # граф реализовывается с помощью хеш-таблицы
# так же приемущество хеш таблице в том что элементы там не упорядочены и добавлять их можно в любом порядке

# НАПРАВЛЕННЫЙ ГРАФ - когда отношения вершин действуют только в одну сторону
# НЕНАПРАВЛЕННЫЙ ГРАФ - когда отношения вершин действуют в обе стороны

# РЕАЛИЗАЦИЯ АЛГОРИТМА
# BFS:
# 1 создать очередь
# 2 извлечь из очереди один элемент
# 3 проверть является ли этот элемент тем который мы ищем 
# 4 добавить всех соседей этого элемента в очередь
# 5 все

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [7],
    6: [],
    7: []
} 

# АЛГОРИТМ ДЕЙКСТРЫ
# Алгоритм поиска в ширину справляется с задачей поиска кратчайшего пути(минимального кол-ва вершин через которые пройти для того чтобы попасть в цель)
# но, если к каждому ребру привязать время в примере с маршруткой из книги или ВЕС
# Вес ребра — значение, поставленное в соответствие данному ребру взвешенного графа
# и по сути алгоритм дейкстры находит путь по графу с минимальным суммарным весом

# выполняется следующим образом:
# 1. найти узел с наименьшей стоимостью
# 2. проверить существует ли более дешевый путь к соседям этого узла и если надо обновить стоимости (это нужно для того чтобы мы корректно сверяли длину пути до определенного узла)
# (показал в tldr)
# 3. все повторяем

# ! важно что алгоритм дейкстры работает только для направленных ацикличных графов
# цикл - это когда мы можем начать из одной вершины и потом вернуться в нее же, путь с обходом по циклу никогда не будет кратчайшим по скольку мы только будем добавлять к суммарному весу значения
# а так же если мы используем алгоритм дейкстры в ненаправленных граффах мы фактически входим в цикл что не имеет смысла для этого алгоритма

# ДЕРЕВЬЯ
