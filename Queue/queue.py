# Implementing a simple Queue in Python


class Queue():

    def __init__(self):
        self.queue = []

    def add(self, val):
        self.queue.append(val)

    def remove(self):
        return self.queue.pop(0)

    def __repr__(self):
        return "Queue(%s)" % str(self.queue)
