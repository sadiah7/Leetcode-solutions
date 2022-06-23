class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                res += chr(ord(i)+32)
            elif ord(i) >= 97 and ord(i) <= 122:
                res+= i
            elif ord(i) >= 48 and ord(i) <= 57:
                res+= i

        
        return res == res[::-1]
        