class Solution(object):
    max_level = 0

    def checkNode(self, n, level):
        if n is None:
            return
        if level > self.max_level:
            self.max_level = level
        self.checkNode(n.left, level + 1)
        self.checkNode(n.right, level + 1)

    def maxDepth(self, root):
        self.checkNode(root, 1)
        return self.max_level
