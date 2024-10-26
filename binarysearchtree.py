class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if root.val < key:
            if root.right is None:
                root.right = BSTNode(key)
            else:
                self._insert(root.right, key)
        else:
            if root.left is None:
                root.left = BSTNode(key)
            else:
                self._insert(root.left, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        res = []
        if root:
            res = self._inorder(root.left)
            res.append(root.val)
            res = res + self._inorder(root.right)
        return res

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self._search(root.right, key)
        return self._search(root.left, key)

# Tests
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print("Inorder Traversal:", bst.inorder())
bst.delete(50)
print("Inorder Traversal after deleting 50:", bst.inorder())
print("Search for 60:", "Found" if bst.search(60) else "Not Found")
print("Inorder Traversal after deleting 50:", bst.inorder())
