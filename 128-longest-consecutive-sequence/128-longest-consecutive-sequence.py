class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        max_count = 0
        for i in nums:
            if i-1 in num_set:
                continue
            count = 1
            while i + 1 in num_set:
                count += 1
                i += 1
            max_count = max(max_count, count)
        
        return max_count