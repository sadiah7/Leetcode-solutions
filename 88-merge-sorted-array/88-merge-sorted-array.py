class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r,temp = m-1, n-1, m+n-1
        while r>=0  and l>=0 and temp>=0:
            if nums2[r] > nums1[l]:
                nums1[temp] = nums2[r]
                r -= 1
            else:
                nums1[temp] = nums1[l]
                l -= 1
            temp -= 1
        while r>= 0:
            nums1[temp] = nums2[r]
            r -= 1
            temp -= 1