class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda box: box[1], reverse=True)
        
        total = 0
        for numberOfBox, unitsPerBox in boxTypes:
            if truckSize > 0:
                numBox = min(truckSize, numberOfBox)
                truckSize -= numBox
                total += numBox*unitsPerBox
            else:
                break
        
        return total