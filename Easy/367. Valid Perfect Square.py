class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = math.sqrt(num)
        if math.ceil(x) == math.floor(x):
            return True
        return False
