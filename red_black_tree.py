class Node:
    def __init__(self, data, color=1):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0, 0)  # NIL nodes are black
        self.root = self.NIL

    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        node.color = 1  # New nodes are red

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        print(" ".join(map(str, result)))

    def _inorder(self, node, result):
        if node != self.NIL:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

# Test
rbt = RedBlackTree()
rbt.insert(55)
rbt.insert(40)
rbt.insert(65)
rbt.insert(60)
rbt.insert(75)
rbt.insert(57)
print("Inorder Traversal of Created Tree:")
rbt.inorder()
