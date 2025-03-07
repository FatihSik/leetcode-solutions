class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0, len(nums) - 1
        pairs = []

        while i < j:
            if nums[i] + nums[j] == k:
                pairs.append((nums[i], nums[j]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -=1
            else:
                i +=1
        return len(pairs)
