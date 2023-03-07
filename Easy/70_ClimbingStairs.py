class Solution(object):
    mem = [0, 1, 2]

    def climbStairs(self, n):
        if n < len(self.mem):
            return self.mem[n]
        self.mem.append(self.climbStairs(n - 1) + self.climbStairs(n - 2))
        return self.mem[n]
