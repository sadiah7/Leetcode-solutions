class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-num for num in target]
        heapify(target)
        while target[0] != -1:
            num = -heappop(target)
            total -= num
            if num <= total or total < 1:
                return False
            num %= total
            total += num
            heappush(target,-num or -total)
        
        return True