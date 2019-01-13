# Implementing a very simple Binary Tree in Python

from queue import Queue


class BinaryTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def __repr__(self):
        return "BinaryNode(%s)" % str(self.data)


def serialize_tree(tree):
    tree_list = []
    queue = Queue()
    queue.add(tree)

    while queue.queue:
        node = queue.remove()
        if node is None:
            tree_list.append(-1)
        else:
            tree_list.append(node.data)

            if node.left:
                queue.add(node.left)
            else:
                queue.add(None)

            if node.right:
                queue.add(node.right)
            else:
                queue.add(None)

    return tree_list


def deserialize_tree(tree_list):
    tree = BinaryTree()
    for data in tree_list:
        if data != -1:
            tree.data = data
            tree.left = BinaryTree()
            tree.right = BinaryTree()


root = BinaryTree()
root.data = 1
root.left = BinaryTree()
root.left.data = 2
root.right = BinaryTree()
root.right.data = 3
root.left.right = BinaryTree()
root.left.right.data = 5
root.right.left = BinaryTree()
root.right.left.data = 6
root.right.right = BinaryTree()
root.right.right.data = 7

#      1
#    /   \
#   2     3
#    \   / \
#     5 6   7

tree_list = serialize_tree(root)
print(tree_list)
# tree = deserialize_tree(root)
