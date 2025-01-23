class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSums = []
        rightSums = []
        for i in range(len(nums)):
            if i == 0:
                leftSums.append((i, nums[i]))
                rightSums.append((len(nums) - i - 1, nums[-(i+1)]))
            else:
                leftSums.append((i, leftSums[i-1][1] + nums[i]))
                rightSums.append((len(nums) - i - 1, rightSums[i-1][1] + nums[-(i+1)]))
        
        
        for x in leftSums:
            if x in rightSums:
                return x[0]
        return -1
