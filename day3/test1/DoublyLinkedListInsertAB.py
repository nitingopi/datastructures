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

    def insert_after(self, searchvalue, value) -> None:
        # 1. list is empty
        if self.head is None:
            return
        else:
            current = self.head
            while searchvalue != current.value:
                current = current.next
                # 2. searchvalue not found    
                if current is None:
                    return
                
            # 3. searchvalue is found            
            else:
                # 3.1. searchvalue is tail
                if current == self.tail:
                    self.add_to_back(value)
                # 3.2. searchvalue is not tail 
                else:
                    node = Node(value)
                    node.prev = current
                    node.next = current.next
                    current.next.prev = node
                    current.next = node

    def insert_before(self, searchvalue, value) -> None:
        # 1. List is empty
        if self.head is None:
            return
        current = self.head
        while current.value != searchvalue:
            current = current.next
            # 2. searchvalue is not found
            if current is None:
                return
        # 3. searchvalue is head
        if current == self.head:
            self.add_to_front(value)
        # 4. searchvalue is not head
        else:
            node = Node(value)
            node.prev = current.prev
            node.next = current    
            current.prev.next = node 
            current.prev = node

    def recursive_front_back(self, node) -> None:
        if node is None:
            return
        self.recursive_front_back(node.next)
        print(node.value)    

    def print_front_to_back(self) -> None:
        self.recursive_front_back(self.head)
        # current = self.head
        # while current is not None:
        #     print(current.value)
        #     current = current.next

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
mylist.print_back_to_front()
print("*"*5)
mylist.print_front_to_back()
mylist.insert_after(8,10)
mylist.insert_before(9,0)
print("*"*10)
mylist.print_front_to_back()
print("*"*5)
mylist.print_back_to_front()
