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

    def insert_after(self, search_value, value) -> None:
        # 1. list is empty
        if self.head is None:
            return
        current = self.head
        while current.value != search_value:
            current = current.next
            # 2. search value is not found
            if current is None:
                return
        # 3. search value is tail   
        if current == self.tail:
            self.add_to_back(value)
            return
        # 4. search value is not tail
        node = Node(value)
        node.prev = current
        node.next = current.next
        current.next.prev = node
        current.next = node


        

    def insert_before(self, search_value, value) -> None:
        # 1. list is empty
        if self.head is None:
            return
        current = self.head
        while current.value != search_value:
            current = current.next
            # 2. search value is not found
            if current is None:
                return    
        # 3. search value is head
        if current == self.head:
            self.add_to_front(value)
            return
        # 4. search value is not head
        node = Node(value)
        node.prev = current.prev
        node.next = current
        current.prev.next = node
        current.prev = node


    def remove(self, search_value) -> None:
        # 1. list is empty
        if self.head is None:
            return
        current = self.head
        while current.value != search_value:
            current = current.next
            # 2. search value is not found
            if current is None:
                return
        # 3. search_value is head and also tail
        if current == self.head == self.tail:
                self.head = None
                self.tail = None
                return
        # 4. search value is head
        if current == self.head:
            current.next.prev = None
            self.head = current.next
            return
        # 5. search_value is tail
        if current == self.tail:
            current.prev.next = None
            self.tail = current.prev
            return
        # 6. search value is neither head or tail
        current.prev.next = current.next
        current.next.prev = current.prev    



    def print_front_to_back(self) -> None:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_back_to_front(self) -> None:
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev           


mylist = List()
mylist.add_to_back(8)
mylist.add_to_front(7)
mylist.add_to_back(9)
mylist.add_to_front(6)
# mylist.print_back_to_front()
# print("*"*5)
# mylist.print_front_to_back()
mylist.insert_after(6,11)
mylist.insert_before(9,0)
mylist.insert_before(7,-1)
# print("*"*10)
mylist.print_front_to_back()
print("*"*5)
mylist.print_back_to_front()
mylist.remove(6)
mylist.remove(9)
mylist.remove(7)
print("*"*10)
mylist.print_front_to_back()
print("*"*5)
mylist.print_back_to_front()
