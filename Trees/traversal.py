"""
BST Traversal Methods
1. PreOrder
2. InOrder
3. PostOrder
"""

from tree import Tree


def preorder(head: Tree):
    """Preorder Traversal of a tree"""
    preorder_list = []

    def pre_order(root):
        nonlocal preorder_list

        preorder_list.append(root.root)

        if root.left:
            pre_order(root.left)

        if root.right:
            pre_order(root.right)

    pre_order(head)
    return preorder_list


def inorder(head: Tree):
    """Inorder Traversal of a tree"""
    inorder_list = []

    def in_order(root):
        nonlocal inorder_list

        if root.left:
            in_order(root.left)

        inorder_list.append(root.root)

        if root.right:
            in_order(root.right)

    in_order(head)
    return inorder_list


def postorder(head: Tree):
    """Postorder Traversal of a tree"""
    postorder_list = []

    def post_order(root):
        nonlocal postorder_list

        if root.left:
            post_order(root.left)

        if root.right:
            post_order(root.right)

        postorder_list.append(root.root)

    post_order(head)
    return postorder_list


if __name__ == "__main__":
    nums = [30, 50, 25, 35, 45, 60, 15, 28, 55, 70]
    tree = Tree(val=40)
    for x in nums:
        tree.add_node(x)

    # Preorder
    pre_ord = preorder(head=tree)
    print("Preorder: ", pre_ord)

    # Inorder
    in_ord = inorder(head=tree)
    print("Inorder: ", in_ord)

    # Postorder
    post_ord = postorder(head=tree)
    print("Postorder: ", post_ord)
