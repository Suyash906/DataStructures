class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        index = 0
        for sh in shift:
            if 0 == sh[0]:
                index -= (sh[1] % len(s))
            else:
                index += (sh[1] % len(s))
        index = index % len(s)
        if index < 0:
            index = len(s) + index
        return s[len(s)-index:] + s[0:len(s)-index]