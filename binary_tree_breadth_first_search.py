# Implementing Breadth-First Search for a Binary Tree

from queue import Queue
from binary_tree import Tree


def breadth_firt_search(value, root):
    """Using a Queue"""
    queue = Queue()
    queue.add(root)

    while queue.queue:
        node = queue.remove()
        print(node)
        if node.data == value:
            return True
        else:
            if node.left:
                queue.add(node.left)

            if node.right:
                queue.add(node.right)

    return False


root = Tree()
root.data = 1
root.left = Tree()
root.left.data = 2
root.right = Tree()
root.right.data = 3
root.left.right = Tree()
root.left.right.data = 5
root.right.left = Tree()
root.right.left.data = 6
root.right.right = Tree()
root.right.right.data = 7

#      1
#    /   \
#   2     3
#    \   / \
#     5 6   7

print(breadth_firt_search(7, root))  # 1 2 3 5 6 7
