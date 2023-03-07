class Solution(object):
    mem = [0, 1]

    def fib(self, n):
        if n < len(self.mem):
            return self.mem[n]
        else:
            res = self.fib(n-1) + self.fib(n-2)
            self.mem.append(res)
            return res
