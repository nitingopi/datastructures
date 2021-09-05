class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # self.prev = None


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None


    def addToBack(self, value):
        node = Node(value)
        if None is self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        

    def addToFront(self, value):
        node = Node(value)
        if None is self.head:
            self.tail = node
        else:
            node.next = self.head
        self.head = node


    def print(self):
        current = self.head
        while current != None :
            print(current.value)
            current = current.next


ll = MyList()
ll.addToBack(4)
ll.addToBack(5)
ll.addToBack(6)
ll.addToFront(3)
ll.addToFront(2)
ll.addToFront(1)

ll.print()
