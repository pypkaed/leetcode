"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
res = []


def visitNode(n):
    if n is not None:
        res.append(n.val)
        for child in n.children:
            visitNode(child)


def preorder(root):
    global res
    res = []
    visitNode(root)
    return res
