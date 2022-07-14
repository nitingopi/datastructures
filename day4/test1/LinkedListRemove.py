from platform import node


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
            self.tail = node
            return
        self.tail.next = node
        self.tail = node


    def add_to_front(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node 

    def insert_after(self, search_value, value) -> None:
        # 1. list is empty
        if self.head is None:
            return
        current = self.head
        while current.value != search_value:
            current = current.next
            # 2. search value is not present
            if current is None:
                return    
        # 3. search value is tail
        if current == self.tail:
            self.add_to_back(value)
            return
        # 4. search value is not tail
        current.next = node
        node.next = current.next  

    def insert_before(self, search_value, value) -> None:
        # 1. if list is empty
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.value != search_value:
            prev = current
            current = current.next
            # 2. if search value is not found
            if current is Node:
                return
        # 3. if search value is head
        if current == self.head:
            self.add_to_front(value)
            return
        # 4. if search value is not head
        node = Node(value)
        prev.next = node
        node.next = current


    def remove(self, value) -> None:
        # 1. if list is empty 
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.value != value:
            prev = current
            current = current.next
            # 3. value is not found
            if current is None:
                return    
        # 2. if value is head == tail
        if current == self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # 4. if value is head
        if current == self.head:
            self.head = current.next
            return
        # 4. if value is tail
        if current == self.tail:
            prev.next = None
            self.tail = prev
            return    
        # 5. if value is middle
        prev.next = current.next


    def print_front_back(self) -> None:
        current = self.head
        while current != None:
            print(current.value)
            current = current.next



my_list = List()
my_list.add_to_back(2)
my_list.add_to_back(3)
my_list.add_to_front(1)
my_list.add_to_back(4)
my_list.print_front_back()
my_list.remove(1)
my_list.remove(3)
my_list.remove(4)
print("*"*5)
my_list.print_front_back()
my_list.insert_after(2,3)
my_list.insert_before(2,1)
my_list.insert_after(3,4)
print("*"*5)
my_list.print_front_back()
