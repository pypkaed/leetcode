# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = 0

def checkNode(n, low, high):
    if n is None:
        return
    global res
    if n.val in range(low, high + 1):
        res += n.val
    checkNode(n.left, low, high)
    checkNode(n.right, low, high)

def rangeSumBST(root, low, high):
    global res
    res = 0
    checkNode(root, low, high)
    return res



print(rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)),
                           TreeNode(15, None, TreeNode(18))), 7, 15))
print(rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
                           TreeNode(15, TreeNode(13), TreeNode(18))), 6, 10))
