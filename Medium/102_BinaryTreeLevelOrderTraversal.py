# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def visitNode(n, level, arr):
    if n is not None:
        if len(arr) <= level:
            arr.append([])
        arr[level].append(n.val)
        visitNode(n.left, level + 1, arr)
        visitNode(n.right, level + 1, arr)


def levelOrder(root):
    res = []
    visitNode(root, 0, res)
    return res
