class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._insert(item, self.root)
    
    def _insert(self, item, cur_node):
        if item < cur_node.item:
            if cur_node.left is None:
                cur_node.left = Node(item)
            else:
                self._insert(item, cur_node.left)
        elif item > cur_node.item:
            if cur_node.right is None:
                cur_node.right = Node(item)
            else:
                self._insert(item, cur_node.right)
        else:
            print("value already in tree")
    
    def delete(self, item):
        if self.root is not None:
            self.root = self._delete(item, self.root)
    
    def _delete(self, item, cur_node):
        print(cur_node.item)
        if cur_node is None:
            return cur_node
        if item < cur_node.item:
            cur_node.left = self._delete(item, cur_node.left)
        elif item > cur_node.item:
            cur_node.right = self._delete(item, cur_node.right)
        else:
            if cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left
            else:
                temp_node = cur_node.right
                while temp_node.left is not None:
                    temp_node = temp_node.left
                cur_node.item = temp_node.item
                cur_node.right = self._delete(temp_node.item, cur_node.right)
        return cur_node

    def search(self, item):
        if self.root is None:
            return False
        else:
            return self._search(item, self.root)
    
    def _search(self, item, cur_node):
        if item == cur_node.item:
            return True
        elif item < cur_node.item and cur_node.left is not None:
            return self._search(item, cur_node.left)
        elif item > cur_node.item and cur_node.right is not None:
            return self._search(item, cur_node.right)
        return False

    def inorder(self):
        def _inorder(cur_node):
            if cur_node.left:
                _inorder(cur_node.left)
            print(cur_node.item, end = ' ')
            if cur_node.right:
                _inorder(cur_node.right)
        _inorder(self.root)
        print()
            


bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(9)
bst.insert(1)
bst.insert(12)
bst.insert(16)
bst.insert(3)
bst.insert(8)

bst.delete(9)
print(bst.search(9))
bst.inorder()