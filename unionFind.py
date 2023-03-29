from aifc import Error


class unionFind:
    size = 0
    sz = []
    # id[i] is the parent of i, if id[i] = i then i is a root node
    id = []

    numComponents = 0

    def __init__(self, externalsize):

        if externalsize <= 0:
            return None
        size = numComponents = externalsize
        for i in range(size, +1):
            self.id[i] = i
            self.sz[i] = 1

    def find(self, p: int) -> int:
        root = p
        while root != self.id[root]: root = self.id[root]

        # root compression
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next
        return root

    def connected(self, i: int, p: int) -> bool:
        return self.find(p) == self.find(i)

    def componentSize(self, p: int) -> int:
        return self.sz[self.find(p)]

    def size(self):
        return self.size

    def components(self) -> int:
        return self.numComponents

    def unify(self, p: int, q: int) -> None:
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2: return
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.id[root1] += self.id[root2]
            self.id[root2] = root1
        self.numComponents -= 1
