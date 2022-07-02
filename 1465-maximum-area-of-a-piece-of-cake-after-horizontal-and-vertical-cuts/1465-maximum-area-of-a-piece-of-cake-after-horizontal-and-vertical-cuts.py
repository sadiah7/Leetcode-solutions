class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHeight = 0
        maxWidth = 0
        prev = 0
        
        for i in horizontalCuts:
            maxHeight = max(maxHeight, i-prev)
            prev = i
        maxHeight = max(maxHeight, h-prev)
        
        prev = 0
        for i in verticalCuts:
            maxWidth = max(maxWidth, i-prev)
            prev = i
        maxWidth = max(maxWidth, w-prev)
        
        return int((maxHeight*maxWidth)%1000000007)