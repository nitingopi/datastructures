class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MyList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def add_to_front(self, value) -> None:
        ref = Node(value)
        if self.head is None:
            self.tail = ref
        else:
            ref.next = self.head
        self.head = ref    

    def add_to_back(self, value) -> None:
        ref = Node(value)
        if self.head is None:
            self.head = ref
        else:
            self.tail.next = ref
        self.tail = ref

    def print(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next 

mylist = MyList()
mylist.add_to_back(3)
mylist.add_to_back(5)
mylist.add_to_front(0)
mylist.add_to_front(-1)
mylist.add_to_back(10)
mylist.print()                     