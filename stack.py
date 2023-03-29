class stack(object):
    def __init__(self):
        arr = []
        position = 0

    def Stack(self, firstElement):
        self.arr.push(firstElement)

    def size(self):
        return len(self.arr)

    def isEmpty(self):
        if self.size() == 0:
            return True

    def pop(self):
        self.arr.pop()

    def peek(self):
        return self.arr[self.size - 1]
