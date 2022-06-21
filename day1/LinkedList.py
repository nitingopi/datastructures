
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,value):
        ref = Node(value)
        print(f"ref {ref}")
        print(f"ref.value {ref.value}")
        if self.head is None:
            self.head = ref
        else:
            self.tail.next = ref    

        self.tail = ref    

    def print(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next    

ls = List()
ls.add(1)
ls.add(2)
ls.add(3)
ls.print()