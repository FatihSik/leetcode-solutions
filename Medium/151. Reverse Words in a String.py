class Solution(object):
    def reverseWords(self, s):
        
        output = []
        words = s.split()
        for i in range(len(words)):
            output.append(words[-(i+1)])
        return ' '.join(str(x) for x in output)
