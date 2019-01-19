# Implementing a Binary Search Tree in Python


class BinaryNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return "BinaryNode(%s)" % str(self.data)


class BinarySearchTree():
    def __init__(self, data):
        self.root = BinaryNode(data)

    def insert(self, data):
        node = self.root
        condition = True
        while condition:
            if data < node.data:
                if node.left:
                    node = node.left
                else:
                    node.left = BinaryNode(data)
                    condition = False
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BinaryNode(data)
                    condition = False

    def __repr__(self):
        return "BST(%s)" % self.root


#      8
#    /   \
#   4     12
#    \   /  \
#     6 10  14

bst = BinarySearchTree(8)
bst.insert(4)
bst.insert(12)
bst.insert(6)
bst.insert(10)
bst.insert(14)
bst.insert(5)
print(bst.root)
print(bst.root.left)
print(bst.root.right)
print(bst.root.left.left)
print(bst.root.left.right)
print(bst.root.left.right.left)
print(bst.root.right.left)
print(bst.root.right.right)