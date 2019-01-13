# Implementing a very simple Binary Tree in Python


class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def __repr__(self):
        return "Node(%s)" % str(self.data)
