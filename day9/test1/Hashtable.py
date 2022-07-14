class Node:
    def __init__(self, key, value) -> None:
        self.next = None
        self.key = key
        self.value = value 

class Table:
    def __init__(self) -> None:
        self.table = {}              
        self.size = 10

    def generate_hash(self, key) -> None:
        return key % self.size    

    def add_item(self, key, value) -> None:
        hash_key = self.generate_hash(key)
        node = Node(key,value)
        if hash_key not in self.table.keys():
            self.table[hash_key] = node
            return
        current = self.table[hash_key]
        back = current
        while current.key != key:
            back = current
            current = current.next
            if current is None:
                node.next = self.table[hash_key]
                self.table[hash_key] = node
                return
                 
        back.next = node
                

    def remove_item(self, key) -> None:
        hash_key = self.generate_hash(key)
        if hash_key not in self.table.keys():
            return
        current = self.table[hash_key]
        # 1. table entry is matching
        if current.key == key:
            self.table[hash_key] = current.next 
            if current.next is None:
                self.table.pop(hash_key)
            return
        back = None    
        while current.key != key:
            back = current
            current = current.next
            # 2. if key is not found   
            if current is None:
                return
        # 3. if key is found    
        back.next = current.next


    def print_table(self) -> None:
        for k,v in self.table.items():
            current = self.table[k]
            while current != None:
                print(f"{current.key}:{current.value}")   
                current = current.next 


table = Table()
table.add_item(1,"Nitin")
table.add_item(2,"Vineet")
table.add_item(1,"Gaurav")
table.print_table()
table.remove_item(1)
table.remove_item(1)
table.remove_item(1)
print("*"*5)
table.print_table()                
