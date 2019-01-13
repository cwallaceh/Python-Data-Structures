# Implementing a Binary Search Tree in Python


class BinaryNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return "BinaryNode(%s)" % str(self.data)


class BinarySearchTree():
    def __init__(self, root):
        self.root = BinaryNode(root)

    def add(self):
        # TODO

    def __repr__(self):
        return "BST(%s)" % self.root


#      8
#    /   \
#   4     12
#    \   /  \
#     6 10  14

bst = BinarySearchTree(8)
print(bst)
