# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkNode(self, n, arr):
        if not n:
            return
        self.checkNode(n.left, arr)
        self.checkNode(n.right, arr)
        arr.append(n.val)

    def postorderTraversal(self, root):
        res = []
        self.checkNode(root, res)
        return res
