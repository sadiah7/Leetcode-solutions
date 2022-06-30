class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        dc = {}
        for letter in s:
            if letter not in dc:
                dc[letter] = 0
            dc[letter] += 1
            
        
        for num in dc.values():
            ans += (num//2) * 2
            if ans%2==0 and num%2==1:
                ans += 1
                
        return ans