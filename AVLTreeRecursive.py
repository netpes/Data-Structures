class AVL:
    class Node:
        height = 0
        bf = 0
        value = None
        left = None
        right = None

        def __init__(self, value):
            self.value = value

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def getText(self):
            return str(self.value)

    root = Node
    nodeCount = 0

    def hieght(self):
        if self.root is None:
            return 0
        return self.root.height

    def size(self):
        return self.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def iscontains(self, value):
        return self.contains(self.root, value)

    def contains(self, node, value):
        if node is None:
            return False
        cmp = 1 if value > node.value else -1 if value < node.value else 0
        if cmp > 0:
            return self.contains(node.left, value)
        if cmp < 0:
            return self.contains(node.right, value)
        return True

    def isinsert(self, value):
        if value is None:
            return False
        if not self.contains(self.root, value):
            self.root = self.insert(self.root, value)
            self.nodeCount += 1
            return True
        return False

    def insert(self, node, value):
        if node is None:
            return self.Node(value)
        cmp = 1 if value > node.value else -1 if value < node.value else 0
        if cmp > 0:
            self.insert(node.left, value)
        else:
            self.insert(node.right, value)
        self.update(node)
        return self.balance(node)

    def update(self, node):
        left_node_height = -1 if node.left is None else node.left.height
        right_node_height = -1 if node.right is None else node.right.height
        node.height = 1 + max(left_node_height, right_node_height)
        node.bf = right_node_height - left_node_height

    def balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.leftLeftCase(node)
            else:
                return self.leftRightCase(node)
        elif node.bf == 2:
            if node.right.bf >= 0:
                return self.rightRightCase(node)
            else:
                return self.rightLeftCase(node)
        return node

    def leftLeftCase(self, node):
        return self.rightRotation(node)

    def leftRightCase(self, node):
        node.left = self.leftRotation(node.left)
        return self.leftLeftCase(node)

    def rightRightCase(self, node):
        return self.leftRotation(node)

    def rightLeftCase(self, node):
        node.right = self.rightRotation(node.right)
        return self.rightRightCase(node)

    def rightRotation(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        self.update(node)
        self.update(newParent)
        return newParent

    def leftRotation(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self.update(node)
        self.update(newParent)
        return newParent

    def isremove(self, element):
        if element is None:
            return False
        if self.contains(self.root, element):
            self.root = self.remove(self.root, element)
            self.nodeCount -= 1
            return True
        return False

    def remove(self, node, element):
        if node is None:
            return None
        cmp = 1 if element > node.value else -1 if element < node.value else 0
        if cmp < 0:
            node.left = self.remove(node.left, element)
        elif cmp > 0:
            node.right = self.remove(node.right, element)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.height > node.right.height:
                    successorValue = self.findMax(node.left)
                    node.value = successorValue
                    node.left = self.remove(node.left, successorValue)
                else:
                    successorValue = self.findMin(node.right)
                    node.value = successorValue
                    node.right = self.remove(node.right, successorValue)
        self.update(node)
        return self.balance(node)

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def findMax(self, node):
        while node.right is not None:
            node = node.right
        return node.value
