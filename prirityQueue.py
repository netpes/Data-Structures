class binaryHeap:
    def __init__(self, elems=None):
        self.heapSize = 0
        self.heapCapacity = 0
        self.heap = []
        if elems is None:
            self.heapCapacity = 1
            self.heap = [None] * self.heapCapacity
        elif isinstance(elems, int):
            self.heapCapacity = len(elems)
            self.heap = [None] * self.heapCapacity
        else:
            self.heapSize = self.heapCapacity = len(elems)
            self.heap = elems.copy()
            for i in range(max(0, (self.heapSize // 2) - 1), -1, -1):
                self.sink(i)

    def isEmpty(self):
        return self.heapSize == 0

    def clear(self):
        for i in range(self.heapCapacity):
            self.heap[i] = None
            self.heapSize = 0

    def size(self):
        return self.heapSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def contains(self, element):
        for i in range(self.heapSize, +1):
            if self.heap[i] == element:
                return True
        return False

    def add(self, element):
        if element == None:
            return False
        if self.heapSize < self.heapCapacity:
            self.heap[self.heapSize] = element
        else:
            self.add(element)
            self.heapCapacity += 1

        self.swim(self.heapSize)

    def less(self, i, j):
        return min(self.heap[j], self.heap[i]) <= 0

    def swin(self, k):
        parent = (k - 1) / 2
        while k > 0 and self.less(k, parent):
            self.swap(parent, k)
            k = parent
            parent = (k - 1) / 2

    def sink(self, k):
        # k is for index
        while (True):
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = left

            if right < self.heapSize and self.less(right, left): smallest = right
            if left >= self.heapSize and self.less(k, smallest): break
            self.swap(smallest, k)
            k = smallest

    def swap(self, i, j):
        store = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = store

    def remove(self, element):
        if element is None: return False
        for i in range(self.heapSize, +1):
            if self.heap[i] == element:
                self.removeAt(i)
                return True
        return False

    def removeAt(self, i):
        if self.isEmpty(): return None
        self.heapSize -= 1
        removedata = self.heap[i]
        self.heap[self.heapSize] = None
        if i == self.heapSize: return removedata
        element = self.heap[i]
        self.sink(i)
        if self.heap[i] == element: self.swin(i)
        return removedata

    def isMin(self, k):
        if k >= self.heapSize: return True
        left = 2 * k + 1
        right = 2 * k + 2
        if left < self.heapSize and not self.less(k, left): return False
        if right < self.heapSize and not self.less(k, right): return False

        return self.isMin(left) and self.isMin(right)
