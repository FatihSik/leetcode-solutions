class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = list(str(x))
        x = [int(i) for i in x if i != '-'] 
        y = x
        y.reverse()

        for i in range(len(x)):
            if x[i] != y[-(1+i)]:
                return False
        
        return True
        
        
