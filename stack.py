# Implementing a Stack in Python without using list method 'pop'


class Stack():

    def __init__(self):
        self.stack = []
        self.idx = 0

    def push(self, val):
        self.stack.append(val)
        self.idx += 1

    def pop(self):
        val = self.stack[self.idx - 1]
        del self.stack[self.idx - 1]
        self.idx -= 1
        return val

    def __repr__(self):
        return "Stack(%s)" % str(self.stack)
