class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = 0
        for token in s.split():
            try:
                # print(token, num)
                if int(token) <= num:
                    return False
                num = int(token)
            except ValueError:
                continue
        return True
            