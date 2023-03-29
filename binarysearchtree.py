class binSearchTree:
    nodeCount = 0
    root = None

    class Node(object, ):
        left, right, element = None, None, None

        def __init__(self, left, right, element):
            self.left = left
            self.right = right
            self.element = element

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.nodeCount

    def isAdded(self, element):
        if self.contains(element):
            return False
        else:
            self.root = self.add(self.root, element)
            self.nodeCount += 1
            return True

    def add(self, node, element):
        if node == None:
            node = self.Node(None, None, node)
        else:
            if (element - node.data) < 0:
                node.left = self.add(node.left, element)
            else:
                node.right = self.add(node.right, element)

        return node

    def isRemoved(self, element):
        if self.contains(element):
            self.root = self.remove(self, self.root, element)
            self.nodeCount -= 1
            return True
        return False

    def remove(self, node, element):
        if node is None: return None
        cmp = element - node.data
        if cmp < 0:
            node.left = self.remove(node.left, element)
        elif cmp > 0:
            node.right = self.remove(node.right, element)
        else:
            if node.left == None:
                rightChild = node.right  # type node
                node.data = None
                node = None
                return rightChild
            elif node.right is None:
                leftChild = node.left
                node.data = None
                node = None
                return leftChild
            else:
                tmp = self.findMin(node.right)
                node.data = tmp.data
                node.right = self.remove(node.right, tmp.data)
        return node

    def findMin(self, node):
        while node.left != None: node = node.left
        return node

    def findMax(self, node):
        while node.right != None: node = node.right
        return node

    def contains(self, node, element):
        if node is None:
            return False
        cmp = element - node.data
        if cmp < 0:
            return self.contains(node.left, element)
        elif cmp > 0:
            return self.contains(node.right, element)
        else:
            return True

    def height(self, node):
        if node is None: return 0
        return max(self.height(node.left), self.height(node.right)) + 1
