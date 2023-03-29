class linkedList(object):
    size = 0
    head = None  # the head of the list
    tail = None  # the tail of the list

    # Define what is Node
    class Node(object):
        data, prev, next = None

        def __init__(self, data, prev, anext):
            self.data = data
            self.prev = prev
            self.next = anext

    def clear(self):
        trav = self.head  # trav is the computer that traverses the list
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, element):
        self.addlast(self, element)

    def addlast(self, element):
        if self.isEmpty():
            self.head = self.tail = self.Node(self, element)
        else:
            self.head.prev = self.Node(self, element, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            return False
        return self.head.data

    def peekLast(self):
        if self.isEmpty():
            return False
        return self.tail.data

    def removeFirst(self):
        if self.isEmpty():
            return False
        # now lets extract the data from the head and link head to the next
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.isEmpty():
            self.tail = None

        return data

    def removeLast(self):
        if self.isEmpty():
            return False
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        if self.isEmpty():
            self.head = None
        return data

    def remove(self, Node):
        if self.Node.prev == None:
            return self.removeFirst()
        if self.Node.next == None:
            return self.removeLast()
        data = self.data
        self.Node.next.prev = self.Node.prev
        self.Node.prev.next = self.Node.next
        self.size -= 1
        return data

    def removeAt(self, index):
        if index < 0 or index > self.size:
            return False
        i = 0
        trav = self.trav
        if index < self.size / 2:
            trav = self.head
            for i in index:
                trav = trav.next
                i += 1
        else:
            i = self.size - 1
            while i >= index:
                trav = trav.prev
                i -= 1
        return self.remove(self, trav)

    def remove(self, obj):
        trav = self.head
        while trav is not None:
            if obj == trav.data:
                self.remove(self, trav)
                return True
        return False

    def indexOf(self, obj):
        index = 0
        trav = self.head
        while trav is not None:
            if trav.data == obj:
                return index
            trav = trav.next
            index += 1
        return -1

    def contains(self, obj):
        return self.indexOf(obj) != -1

    class trav:

        def __iter__(self):
            trav = self.head
            return trav

        def __next__(self):
            data = self.trav.data
            self.trav = self.trav.next
            return data
