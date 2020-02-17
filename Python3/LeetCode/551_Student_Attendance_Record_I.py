class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0        
        for char in s:
            if char == 'A':
                countA += 1
        
        Lflag = False
        for index in range(len(s)-2):
            if s[index] == "L" and s[index+1] == "L" and s[index+2] == "L":
                Lflag = True
                break
        
        if  countA > 1 or True == Lflag:
            return False
        return True
