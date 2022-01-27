class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # bst can't have duplicates

        if data < self.data:
            # add to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit left subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def delete_using_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

        if val < self.data:
            # value may be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # value may be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BSTNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

class BST:
    pass


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    #print(numbers_tree.in_order_traversal())
    #print(numbers_tree.search(20))
    print(numbers_tree.find_max())
    numbers_tree.delete_using_max(20)
    print(numbers_tree.in_order_traversal())
