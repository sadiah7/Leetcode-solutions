class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ls = []
        x = numRows
        down, up = 1, 0
        for i in s:
            if down:
                ls.append([i,x])
                x -= 1
                if x==0:
                    up = 1
                    down = 0
                    x = 2
            else:
                ls.append([i,x])
                x += 1
                if x == numRows+1:
                    down = 1
                    up = 0
                    x = numRows-1
        # print(ls)
        x = numRows
        op = ""
        for i in range(numRows):
            for letter, num in ls:
                if num == x:
                    op += letter
            x -= 1
        return op