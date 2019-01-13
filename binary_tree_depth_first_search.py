# Implementing Depth-First Search for a Binary Tree

from stack import Stack
from binary_tree import Tree


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
            if node.right:
                stack.push(node.right)

            if node.left:
                stack.push(node.left)

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

print(depth_first_search(7, root))  # 1 2 5 3 6 7
