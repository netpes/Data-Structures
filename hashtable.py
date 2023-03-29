from email.policy import default


class hashTable:
    loadFactor, capacity, threshold, modificationCount, usedBuckets, keyCount = 0
    keys = []
    values = []
    Tombstone = object()
    defaultCapacity = 7
    defaultLoadFactor = 0.65

    def __init__(self, capacity, loadFactor):
        if capacity and loadFactor is None:
            pass
        elif capacity is not None and loadFactor is None:
            self.capacity = capacity
        elif loadFactor is not None and capacity is None:
            self.loadFactor = loadFactor
        else:
            self.loadFactor = loadFactor
            self.capacity = max(capacity, self.defaultCapacity)
            self.threshold = self.capacity * self.loadFactor

    def setupProbing(self, key):
        return None

    def probe(self, x):
        return None

    def adjustCapacity(self, capacity):
        return None

    def increaseCapacity(self):
        self.capacity = (self.capacity * 2) + 1

    def clear(self) -> None:
        for i in range(self.capacity, +1):
            self.keys[i] = None
            self.values[i] = None
        self.keyCount = self.usedBuckets = 0
        self.modificationCount -= 1

    def size(self) -> int:
        return self.keyCount

    def getCapacity(self) -> int:
        return self.capacity

    def isEmpty(self) -> bool:
        return self.keyCount == 0

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def containsKey(self, key):
        return self.hasKey(key)

    def keys(self):
        hashableKeys = []
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys is not self.Tombstone:
                hashableKeys.append(self.keys[i])
        return hashableKeys

    def resizeTable(self):
        self.increaseCapacity()
        self.adjustCapacity()
        self.threshold = self.capacity * self.loadFactor
        keytabletmp = self.keys
        self.keys = []
        oldkeytable = keytabletmp

        valuetabletmp = self.values
        self.values = []
        oldvaluetable = valuetabletmp

        self.keyCount = self.usedBuckets = 0
        for i in range(len(oldvaluetable), +1):
            if oldkeytable[i] is not None and oldvaluetable[i] is not self.Tombstone:
                self.insert(oldkeytable[i], oldvaluetable)
            oldvaluetable[i] = None
            oldkeytable[i] = None

    def normalizeIndex(self, keyHash):
        return (keyHash & 0x7FFFFFFFF) % self.capacity

    def GCD(self, a, b):
        if b == 0: return a
        return self.GCD(self, b, a % b)

    def insert(self, key, value):
        if key is None: return False
        if self.usedBuckets >= self.threshold: self.resizeTable()

        self.setupProbing(key)
        offset = self.normalizeIndex(key.hashCode())
        j = -1
        x = 1
        i = offset
        while offset:
            i = self.normalizeIndex(offset + self.probe(x + 1))
            if self.keys[i] is self.Tombstone:
                if j == -1: j = 1
            elif self.keys[i] is not None:
                if self.keys[i] is key:
                    oldvalue = self.values[i]
                    if j == -1:
                        self.values[i] = value
                    else:
                        self.values[i] = None
                        self.keys[j] = key
                        self.values[i] = value
                    self.modificationCount += 1
                    return oldvalue
            else:
                if j == -1:
                    self.usedBuckets += 1
                    self.keyCount += 1
                    self.keys[i] = key
                    self.values[i] = value
                else:
                    self.keyCount += 1
                    self.keys[j] = key
                    self.values[j] = value
                self.modificationCount += 1
                return None

    def hasKey(self, key):
        if key is None:
            return False
        self.setupProbing(key)
        offset = self.normalizeIndex(key.hashCode())
        j = -1  # j is the index of tombstone
        x = 1
        i = offset
        while offset:
            i = self.normalizeIndex(offset + self.probe(x + 1))
            if self.keys[i] == self.Tombstone:
                if j == -1: j = 1
            elif self.keys[i] is not None:
                if self.keys[i] == key:
                    if j != -1:
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = self.Tombstone
                        self.values[i] = None
                    return True
                else:
                    return False

    def get(self, key):
        if key is None: return None
        self.setupProbing(key)
        offset = self.normalizeIndex(key.hashCode())
        j = -1  # j is the index of tombstone
        x = 1
        i = offset
        while offset:
            i = self.normalizeIndex(offset + self.probe(x + 1))
            if self.keys[i] == self.Tombstone:
                if j == -1: j = 1
            elif self.keys[i] is not None:
                if self.keys[i] == key:
                    if j != -1:
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = self.Tombstone
                        self.values[i] = None
                        return self.values[j]
                    else:
                        return self.values[i]
            else:
                return None

    def remove(self, key):
        if key is None: return None
        offset = self.normalizeIndex(key.hashCode())
        j = -1  # j is the index of tombstone
        x = 1
        i = offset
        while offset:
            i = self.normalizeIndex(offset + self.probe(x + 1))
            if self.keys[i] == self.Tombstone:
                pass
            if self.keys[i] is None:
                return None
            if self.keys[i] == key:
                self.keyCount -= 1
                self.modificationCount -= 1
                oldValue = self.values[i]
                self.keys[i] = self.Tombstone
                self.values[i] = None
                return oldValue
