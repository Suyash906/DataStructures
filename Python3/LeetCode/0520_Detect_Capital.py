class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:return True
        all_lower_case = True
        for char in word:
            if char.isupper():
                all_lower_case = False
                break
        if all_lower_case:return True
        
        all_upper_case = True
        for char in word:
            if char.islower():
                all_upper_case = False
                break
        if all_upper_case:return True
        
        if word[0].islower():
            return False
        
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        return True
        
