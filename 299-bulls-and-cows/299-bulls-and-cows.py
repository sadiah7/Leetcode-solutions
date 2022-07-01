class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        temp = secret[:]
        bulls,cows = 0,0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            
        for i in range(len(guess)):
            if guess[i] in temp:
                cows += 1
                temp = temp.replace(guess[i],' ',1)
            
            
        return str(bulls)+'A'+str(cows-bulls)+'B'
                
            
        
        