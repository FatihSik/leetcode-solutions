class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        output = []
        for i in candies:
            if max(candies) > (i + extraCandies):
                output.append(False)
            else:
                output.append(True)
        return output
