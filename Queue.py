import linkedlist as linkedlist


class Queue:
    list = linkedlist.linkedList()

    def __init__(self, firstelement):
        self.offer(firstelement)

    def size(self):
        return self.list.size()

    def isEmpty(self):
        return self.list.size() == 0

    def peek(self):
        if self.isEmpty() == 0:
            return self.list.peekFirst()

    def pool(self):
        if self.isEmpty() == 0:
            return self.list.removeFirst()

    def offer(self, element):
        self.list.addlast(element)
