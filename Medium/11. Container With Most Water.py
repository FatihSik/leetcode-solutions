class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        bigArea = 0
        while i < j:
            area = (j - i)*min(height[i], height[j])
            bigArea = max(area, bigArea)

            if height[i] > height[j]:
                j -= 1
            else:
                i+= 1 
        return bigArea
