from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value) -> Node:
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node    
        return node

    def print(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


mylist = List()
mylist.add(2)
mylist.add(3)
mylist.print()