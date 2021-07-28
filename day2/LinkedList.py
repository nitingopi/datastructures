
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self,value):
        ref = Node(value)
        if self.head is None:
            self.head = ref
        else:
            self.tail.next = ref    
        self.tail = ref    

    def addToFront(self,value):
        ref = Node(value)
        if self.head is None:
            self.tail = ref
        else:
            ref.next = self.head
      
        self.head = ref

    def print(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next    

ls = List()
ls.addToBack(1)
ls.addToBack(2)
ls.addToBack(3)
ls.addToFront(4)
ls.addToFront(5)
ls.addToBack(6)
ls.print()