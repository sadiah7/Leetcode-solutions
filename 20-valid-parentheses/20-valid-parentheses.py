class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        start = ['(', '[', '{']
        dc = { '(' : ')', '[': ']', '{' : '}'}
        for brac in s:
            if brac in start:
                top += 1
                stack.append(brac)
            else:
                if top == -1: #if the first character is closing bracket
                    return False
                if dc[stack[top]] != brac:
                    return False
                stack.pop(top)
                top -= 1
        
        # print(top)
        if top == -1:
            return True
        return False
                