class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        up = [0]*len(nums)
        down = [0]*len(nums)
        
        up[0], down[0] = 1,1
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] <nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        
        return max(down[len(nums)-1], up[len(nums)-1])