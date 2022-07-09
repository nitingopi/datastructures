class Node:
    def __init__(self, value) -> None:
       self.value = value
       self.prev = None
       self.next = None 

class MyDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def add_to_back(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node   

    def add_to_front(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def print_forwards(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_backwards(self) -> None:
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev


mylist = MyDoublyLinkedList()
mylist.add_to_back(2)
mylist.add_to_front(-1)
mylist.add_to_front(-2)
mylist.add_to_back(3)
mylist.add_to_front(-3)
mylist.add_to_front(-4)
mylist.add_to_back(5)

# mylist.print_backwards()
mylist.print_forwards()    