class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackSolution(s):
            stack = []
            for i in range(len(s)):
                if s[i] != '#':
                    stack.append(s[i])
                else:
                    if len(stack) != 0:
                        stack.pop()
            
            return ''.join(stack)
        
        if stackSolution(s)==stackSolution(t):
            return True
        return False