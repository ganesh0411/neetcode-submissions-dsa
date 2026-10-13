from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        target = Counter(s1)
        while r <= len(s2):
            if Counter(s2[l:r]) == target:
                return True
            else:
                l, r = l+1, r+1
        return False