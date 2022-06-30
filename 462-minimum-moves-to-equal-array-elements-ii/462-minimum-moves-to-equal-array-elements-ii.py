class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mid = (0 + len(nums))//2
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i] - nums[mid])
        
        return count