# Linked list implementation in Python


class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "%s→%s" % (self.value, self.next)


class LinkedList():

    def __init__(self, value):
        self.first = Link(value)
        self.current = self.first

    def __repr__(self):
        return 'LinkedList(%s)' % self.first

    def insert(self, value):
        self.current.next = Link(value)
        self.current = self.current.next

    def remove(self):
        """TODO"""
        pass


linked_list = LinkedList(2)
linked_list.insert(4)
linked_list.insert(3)
linked_list.insert(7)
print(linked_list)
