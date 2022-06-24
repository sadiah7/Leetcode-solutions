class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1 and digits[i] < 9:
                digits[i] += 1
                return digits
            total = digits[i] + carry
            if total > 9:
                digits[i] = total - 10
                carry = 1
            else:
                digits[i] = total
                carry = 0
        if carry == 1:
            digits.insert(0,1)
        return digits