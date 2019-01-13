# Implementing a very simple N-ary Tree in Python

#      1
#    / | \
#   2  3  4
#  / \    |
# 5   6   7

from queue import Queue
from stack import Stack


class Node():

    def __init__(self, data):
        self.children = []
        self.data = data

    def add_children(self, data):
        self.children.append(Node(data))

    def __repr__(self):
        return "Node(%s)" % str(self.data)


def breadth_first_search(value, root):
    """Using a Queue"""
    queue = Queue()
    queue.add(root)

    while queue.queue:
        node = queue.remove()
        print(node)
        if node.data == value:
            return True
        else:
            for child in node.children:
                queue.add(child)

    return False


def depth_first_search(value, root):
    """Using a Stack"""
    stack = Stack()
    stack.push(root)

    while stack.stack:
        node = stack.pop()
        print(node)
        if node.data == value:
            return True
        else:
            for child in reversed(node.children):
                stack.push(child)

    return False


tree = Node(1)
tree.add_children(2)
tree.children[0].add_children(5)
tree.children[0].add_children(6)
tree.add_children(3)
tree.add_children(4)
tree.children[2].add_children(7)
print(breadth_first_search(7, tree))
print(depth_first_search(7, tree))
