class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dc = {}
        temp = []
        for i in nums:
            if i not in dc:
                dc[i] = 0
            dc[i] += 1
        
        for i in dc:
            if dc[i] == 1 and (i-1) not in dc and (i+1) not in dc:
                temp.append(i)
                
        return temp
                
        