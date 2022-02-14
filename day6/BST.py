class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None


    def addNode(self, current, value):
        if current is None:
            return Node(value)
     
        if value < current.value:
            current.left = self.addNode(current.left, value)
        
        if value > current.value:
            current.right = self.addNode(current.right, value)
        return current    

    def printInOrder(self, current):
        if current:
            self.printInOrder(current.left)
            print(current.value)
            self.printInOrder(current.right)

    def printPreOrder(self, current):
        if current:
            print(current.value)
            self.printPreOrder(current.left)
            self.printPreOrder(current.right)

    # def printPostOrder(self, current):
    #     if current:
    #         self.print(current.left)



ped = Tree()
# ped.root = None
ped.root = ped.addNode(ped.root, 5)
ped.addNode(ped.root, 7)
ped.addNode(ped.root, 9)
ped.addNode(ped.root,1)
ped.addNode(ped.root,3)
# ped.printInOrder(ped.root)
ped.printPreOrder(ped.root)

