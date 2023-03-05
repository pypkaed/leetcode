# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


def binsearch(root, n, trace):
    curr = root
    if curr is None:
        return
    trace.append(curr)
    if curr.val == n.val:
        return
    if curr.val < n.val:
        binsearch(curr.right, n, trace)
    else:
        binsearch(curr.left, n, trace)


def lowestCommonAncestor(root, p, q):
    curr = root
    p_trace = []
    q_trace = []
    binsearch(root, p, p_trace)
    binsearch(root, q, q_trace)
    for i in range(len(min(p_trace, q_trace, key=len))-1, -1, -1):
        if p_trace[i] == q_trace[i]:
            return p_trace[i]


print(lowestCommonAncestor
      (TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
       , TreeNode(2), TreeNode(8)))
