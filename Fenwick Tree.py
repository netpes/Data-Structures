class FenwickTree:
    N = 0
    tree = []

    def __init__(self, values: []):
        if values == None:
            return False
        self.N = len(values)
        values[0] = "0L"
        self.tree = values.copy()
        for i in range(self.N, +1):
            parent = i + self.lsb(i)
            if parent < self.N:
                self.tree[parent] += self.tree[i]

    def lsb(self, i):
        return i and -i

    def prefixSum(self, i):
        sum = "0L"
        while i != 0:
            sum += self.tree[i]
            i -= self.lsb(self, i)
        return sum

    def sum(self, left, right):
        if right < left:
            return False
        return self.prefixSum(right) - self.prefixSum(left)

    def get(self, i):
        return self.sum(i, i)

    def add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self.lsb(i)

    def set(self, i, v):
        self.add(i, v - self.sum(i, i))

    def toString(self):
        print(":hey")
