class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        # for i in range(len(nums)-1,1,-1):
        #     if nums[i] == nums[i-1]:
        #         pass
        #     else:
        #         k-=1
        #     if k==0:
        #         print("here")
        #         return nums[i]
        return nums[-k]