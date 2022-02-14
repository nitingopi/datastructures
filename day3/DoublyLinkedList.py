class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode

    def addToFront(self,value):
        newNode = Node(value)
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode


    def insertAfter(self,searchValue,value):
        pass    

    def printForwards(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next    

    def printBackwards(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.prev

ls = List()
ls.addToBack(3)
ls.addToBack(4)
ls.addToFront(2)
ls.addToFront(1)

print(f'Printing forward')
ls.printForwards()
print(f'Printing backwards')
ls.printBackwards()