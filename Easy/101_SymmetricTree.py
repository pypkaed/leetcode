# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkNode(self, nl, nr):
        if not nl and not nr:
            return True
        if (nl and not nr) or (not nl and nr):
            return False
        if nl.val != nr.val:
            return False
        return self.checkNode(nl.left, nr.right) and self.checkNode(nl.right, nr.left)

    def isSymmetric(self, root):
        if not root:
            return False
        return self.checkNode(root, root)
