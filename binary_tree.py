# Implementing a very simple Binary Tree in Python


class BinaryTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def __repr__(self):
        return "Node(%s)" % str(self.data)
