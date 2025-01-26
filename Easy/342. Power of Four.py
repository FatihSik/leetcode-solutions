class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n in [2**x for x in range(0,32,2)]:
            return True
        return False
