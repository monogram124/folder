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
