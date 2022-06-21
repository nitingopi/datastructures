class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value) -> Node:
        ref = Node(value)
        if self.head is None:
            self.head = ref
        else:
            current = self.tail
            current.next = ref

        self.tail = ref


    def print(self) -> None:
        current = self.head
        if current is None:
            print("list is empty")
        else:
            printstr = ""
            while current is not None:
                # print(type(current))
                # print(f"{current.value} -> ")
                printstr += f" {current.value} ->"
                current = current.next    
            print(printstr)    

mylist = List()
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.print()                