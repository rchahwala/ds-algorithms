"""
Find the diameter of a BST
"""

from tree import Tree


def diameter_of_tree(head: Tree):
    max_ = 0

    def dfs(root):
        nonlocal max_

        if root is None:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        max_ = max(max_, left + right)
        return max(left, right) + 1

    dfs(head)
    return max_


if __name__ == "__main__":
    nums = [10, 4, 7, 3, 2, 1]
    tree = Tree(val=6)
    for x in nums:
        tree.add_node(x)
    diameter = diameter_of_tree(head=tree)
    print(diameter)
