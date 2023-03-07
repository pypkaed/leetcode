class MyQueue(object):

    def __init__(self):
        self.s1 = []  # first stack normal
        self.s2 = []  # second stack reversed (reading)

    def push(self, x):
        self.s1.append(x)  # [1,2]
        self.s2 = list(reversed(self.s1))

    def pop(self):
        # s1: [1, 2, 3]
        # s2: [] -> [3, 2, 1] -> [3, 2]
        # s1 = [2, 3]
        self.s2 = list(reversed(self.s1))
        res = self.s2.pop()
        self.s1 = list(reversed(self.s2))
        return res

    def peek(self):
        return self.s2[len(self.s2) - 1]

    def empty(self):
        return len(self.s1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()