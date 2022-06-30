# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high = 1, n
        while(low <= high):
            mid = (low + high)//2
            if(low == high):
                return low
            elif isBadVersion(mid):
                high = mid
            elif not isBadVersion(mid):
                low = mid + 1
        
        