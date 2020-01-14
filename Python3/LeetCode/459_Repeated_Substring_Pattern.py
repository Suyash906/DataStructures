class Solution:
    def repeatedSubstringPattern1(self, s: str) -> bool:
        slen = len(s)
        mid = slen//2
        
        while mid >= 0:
            curr = s[0:mid]
            if 0 == len(s.replace(curr,"")):
                return True
            mid = mid - 1
        return False

    
    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s * 2)[1:-1]