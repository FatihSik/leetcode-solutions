class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            x1 = 1
            x2 = 0
            output = 0
            for i in range(1,n):
                output = x1 + x2
                x2 = x1
                x1 = output
        return output
