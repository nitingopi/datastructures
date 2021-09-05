class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class MyDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self, value):
        node = Node(value)
        if None is self.head:
            self.head = node    
        else:
            self.tail.next = node 
            node.prev = self.tail
        self.tail = node 

    def addToFront(self, value):
        node = Node(value)
        if None is self.head:
            self.tail = node
        else:
            self.head.prev = node 
            node.next = self.head         
        self.head = node 
       
    def printForwards(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def printBackwards(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev 

dll = MyDoublyLinkedList()
dll.addToBack(4)
dll.addToBack(5)
dll.addToBack(6)
dll.addToFront(3)
dll.addToFront(2)
dll.addToFront(1)

# dll.printForwards()
dll.printBackwards()