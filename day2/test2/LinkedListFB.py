class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_to_back(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node                

    def add_to_front(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node 

    def print(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

mylist = List()
mylist.add_to_back(4)
mylist.add_to_front(3)
mylist.add_to_back(5)
mylist.add_to_front(2)
mylist.print()
