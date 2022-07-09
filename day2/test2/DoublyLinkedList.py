class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
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
            node.prev = self.tail
            self.tail.next = node
        self.tail = node 

    def add_to_front(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node        

    def print_front_back(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next 

    def print_back_front(self) -> None:
        current = self.tail 
        while current is not None:
            print(current.value)
            current = current.prev 

mylist = List()
mylist.add_to_back(6)
mylist.add_to_front(5)
mylist.add_to_back(7)
mylist.add_to_front(4)
mylist.print_back_front()
print("*"*5)
mylist.print_front_back()                     

