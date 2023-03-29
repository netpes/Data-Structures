class DynamicArray(object):
    capacity = 0
    length = 0
    array = []

    def DynamicArray(self, capacity):
        if self.capacity > 0:
            return False
        self.capacity = capacity
        arr = object(capacity)

    def size(self):
        return self.length

    def isEmpty(self):
        return self.size() == 0

    def get(self, index):
        return self.array[index]

    def set(self, index, element):
        if self.capacity < index:
            return False
        self.array[index] = element

    def clear(self):
        for i in range(self.capacity):
            self.array[i] = None

    def add(self, element):
        if self.length + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
            new_array = object(self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.length + 1] = element

    def removeAt(self, index):
        if self.length < index:
            return False
        new_array = object(self.capacity)
        j = 0
        for i in self.length:
            if i == index:
                j = j - 1
            else:
                new_array[j] = self.array[i]
            j = j + 1
        self.array = new_array
        self.capacity = self.length - 1

    def remove(self, element):
        index = self.indexOf(self, element)
        if index == -1:
            return False
        self.removeAt(self, index)
        return True

    def indexOf(self, element):
        if element in self.array:
            index = self.array.index(element)
            return index
        else:
            return -1

    def iterator(self):
        index = 0

        def hasNext(self):
            return self.index > self.length

        def nextOne(self):
            self.index += 1
            return self.array[self.index]
