class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = -1
        else:
            negative = 1
        x = abs(x)
        y = list(str(x))
        y.reverse()
        reverse = int(''.join(y))
        if reverse <= 2**31 - 1:
            return reverse * negative
        else:
            return 0
