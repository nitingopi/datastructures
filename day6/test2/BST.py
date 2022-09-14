class Node:
    def __init__(self, value) -> None:
        self.left = self.right = None
        self.value = value

class Tree:
    def insert(self, root, value) -> Node:
        if root is None:
            return Node(value)
        if value <= root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)    
        return root    

    def print_inorder(self, current) -> None:
        if current:
            self.print_inorder(current.left)
            print(current.value)
            self.print_inorder(current.right)

    def print_preorder(self, current) -> None:
        if current:
            print(current.value)
            self.print_preorder(current.left)
            self.print_preorder(current.right)

    def print_postorder(self, current) -> None:
        if current:
            self.print_postorder(current.left)
            self.print_postorder(current.right)
            print(current.value)        

    def search(self, current, value) -> bool:
        if current is None:
            return False
        if value < current.value:
            return self.search(current.left, value)
        elif value == current.value:
            return True    
        else:
            return self.search(current.right, value)        

    def max_height(self, root) -> int:
        if root is None:
            return -1
        return max(self.max_height(root.left), self.max_height(root.right))+1



mytree = Tree()
root = None
root = mytree.insert(root, 7)
root = mytree.insert(root, 1)
root = mytree.insert(root, 4)
root = mytree.insert(root, 2)
root = mytree.insert(root, 5)
root = mytree.insert(root, 3)
root = mytree.insert(root, 6)
mytree.print_inorder(root)
print('*'*5)
mytree.print_preorder(root)
print('*'*5)
mytree.print_postorder(root)
print(mytree.search(root, 7))
print(mytree.search(root, 3))
print(mytree.search(root, 6))
print(mytree.search(root, 11))
print(mytree.search(root, 5))
print(mytree.max_height(root))