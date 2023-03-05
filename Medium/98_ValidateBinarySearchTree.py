# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(n, arr):
    if n is None:
        return
    traversal(n.left, arr)
    arr.append(n)
    traversal(n.right, arr)


def search(root, n):
    if root is None:
        return
    if root == n:
        return root
    if root.val == n.val:
        return
    if root.val > n.val:
        return search(root.left, n)
    else:
        return search(root.right, n)


def isValidBST(root):
    nodes = []
    traversal(root, nodes)
    for node in nodes:
        if search(root, node) != node:
            return False
    return True


print(isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
print(isValidBST(TreeNode(2, TreeNode(1, None, TreeNode(3)))))
print(isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))
print(isValidBST(TreeNode(2, TreeNode(2), TreeNode(2))))
print(isValidBST(TreeNode(32, TreeNode(26, TreeNode(19, None, TreeNode(27))), TreeNode(47, None, TreeNode(56)))))
