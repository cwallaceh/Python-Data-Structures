
from queue import Queue
from binary_tree import BinaryTree


def check_if_binary_search_tree(root):
    """Using a Queue"""
    queue = Queue()
    queue.add(root)

    while queue.queue:
        node = queue.remove()
        print(node)
        if node.left:
            # If left node, check it is smaller
            if node.left.data < node.data:
                queue.add(node.left)
            else:
                return False
        if node.right:
            # If right node, check it is greater
            if node.right.data > node.data:
                queue.add(node.right)
            else:
                return False

    return True


root = BinaryTree()
root.data = 8
root.left = BinaryTree()
root.left.data = 4
root.right = BinaryTree()
root.right.data = 12
root.left.right = BinaryTree()
root.left.right.data = 6
root.right.left = BinaryTree()
root.right.left.data = 10
root.right.right = BinaryTree()
root.right.right.data = 14

#      8
#    /   \
#   4     12
#    \   /  \
#     6 10  14

print(check_if_binary_search_tree(root))  # 8 4 12 6 10 14
