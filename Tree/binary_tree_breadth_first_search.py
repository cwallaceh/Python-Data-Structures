# Implementing Breadth-First Search for a Binary Tree

from queue import Queue
from binary_tree import BinaryTree


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
            if node.left:
                queue.add(node.left)

            if node.right:
                queue.add(node.right)

    return False


# root = BinaryTree()
# root.data = 1
# root.left = BinaryTree()
# root.left.data = 2
# root.right = BinaryTree()
# root.right.data = 3
# root.left.right = BinaryTree()
# root.left.right.data = 5
# root.right.left = BinaryTree()
# root.right.left.data = 6
# root.right.right = BinaryTree()
# root.right.right.data = 7

#      1
#    /   \
#   2     3
#    \   / \
#     5 6   7

# print(breadth_first_search(7, root))  # 1 2 3 5 6 7
