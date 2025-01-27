class Solution:
    def integerBreak(self, n: int) -> int:
        if 0 < n < 4:
            return n - 1
        elif n == 0:
            return 0
        else:
            if n % 3 == 0:
                return int(3**(n/3))
            elif n % 3 == 1:
                return 4 * int(3**((n-4)/3))
            else:
                return 2 * 3**int(n/3)
