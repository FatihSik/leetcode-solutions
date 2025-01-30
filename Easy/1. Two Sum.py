class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if target - x in seen:
                return [seen[complement], i]
            else:
                seen[x] = i
