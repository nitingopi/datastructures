class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MyList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value) -> None:
        ref = Node(value)
        if self.head is None:
            self.head = ref
        else:
            # current = self.tail
            # current.next = ref
            self.tail.next = ref
        self.tail = ref 

    def print(self) -> None:
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current is not None:
                print(f"{current.value}")
                current = current.next


myls = MyList() 
myls.add(9)
myls.add(8)
myls.print()               