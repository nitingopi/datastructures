from xmlrpc.client import Boolean


class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None

    def add(self, current, value) -> Node:
        if current is None:
            return Node(value)
            

        if value < current.value:
            current.left =  self.add(current.left, value)

        if value > current.value:
            current.right =  self.add(current.right, value)   

        return current 

    def print_pre_order(self, current) -> None:
        if current:
            print(current.value)
            self.print_pre_order(current.left)
            self.print_pre_order(current.right)

    def print_in_order(self, current) -> None:
        if current:
            self.print_in_order(current.left)
            print(current.value)
            self.print_in_order(current.right)

    def print_post_order(self, current) -> None:
        if current:
            self.print_post_order(current.left)
            self.print_post_order(current.right)
            print(current.value)   

    def search(self, current, search_value) -> Boolean:
        # 1. if value is found return true
        if current:
            if current.value == search_value:
                return True
            if search_value < current.value:
                return self.search(current.left,search_value)
            if search_value > current.value:
                return self.search(current.right, search_value)        
        # 2. return false
        return False  

    # def remove(self, current, value) -> None:
    #     if current is None:
    #         return
    #     if current.value == value:
    #         if current.left == current.right == None:
    #             current = None
    #             return
    #         if current.left == None:
                


tree = Tree()
root = None
root = tree.add(root, 3)
tree.add(root, 5)
tree.add(root, 2)
print("IN ORDER")             
tree.print_in_order(root)
print('*'*5)
print("PRE ORDER")
tree.print_pre_order(root)
print('*'*5)
print("POST ORDER")
tree.print_post_order(root)
print('*'*5)
print(tree.search(root,1))
