"""
Class to create a Binary Search Tree
"""


class Tree:
    def __init__(self, val: int):
        self.left = None
        self.root = val
        self.right = None

    def add_node(self, val: int):
        if self.root is None:
            return

        if val > self.root:
            if self.right:
                self.right.add_node(val=val)
            else:
                self.right = Tree(val=val)
        else:
            if self.left:
                self.left.add_node(val=val)
            else:
                self.left = Tree(val=val)


if __name__ == "__main__":
    nums = [10, 4, 7, 3, 2, 1]
    tree = Tree(val=6)
    for x in nums:
        tree.add_node(x)
