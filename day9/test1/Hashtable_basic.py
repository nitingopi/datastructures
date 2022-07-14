class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self) -> None:
        self.table = {}
        self.size = 10

    def generate_hash(self, value) -> int:
        return value % self.size

    def add_item(self, value) -> None:
        hash_value = self.generate_hash(value)
        node = Node(value)
        if hash_value not in self.table.keys():
            self.table[hash_value] = node
            return
        if hash_value in self.table.keys():
            node.next = self.table[hash_value]
            self.table[hash_value] = node

    def print_table(self) -> None:
        for k,v in self.table.items():
            current = v
            while current != None:
                print(current.value)
                current = current.next

    def remove_item(self, value) -> None:
        hash_value = self.generate_hash(value)
        if hash_value in self.table.keys():
            current = self.table[hash_value]
            back = None
            while current.value != value:
                back = current
                current = current.next
                if current is None:
                    return
            if current == self.table[hash_value]:
                self.table[hash_value] = current.next 
                return       
            back.next = current.next


hashtable = Hashtable()
hashtable.add_item(11)
hashtable.add_item(12)
hashtable.add_item(13)
hashtable.add_item(14)
hashtable.add_item(15)
hashtable.add_item(16)
hashtable.add_item(17)
hashtable.add_item(18)
hashtable.add_item(19)
hashtable.add_item(20)
hashtable.add_item(21)
hashtable.add_item(22)
hashtable.add_item(23)
hashtable.add_item(24)
hashtable.add_item(25)
hashtable.add_item(26)
hashtable.add_item(27)
hashtable.add_item(28)
hashtable.add_item(29)
hashtable.add_item(30)
hashtable.add_item(30)




hashtable.print_table()
hashtable.remove_item(11)
hashtable.remove_item(21)
print("*"*5)
hashtable.print_table()



