class Solution(object):
    def isSubsequence(self, s, t):
        
        ticker = 0
        if s == '':
            return True
        for i in list(t):
            if ticker < len(s) and i == s[ticker]:
                ticker += 1
        if ticker != len(s):
            return False
        else:
            return True
