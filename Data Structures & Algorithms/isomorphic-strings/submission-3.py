class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        mappingST = {}
        mappingTS = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in mappingST and mappingST[c1] != c2) or
                (c2 in mappingTS and mappingTS[c2] != c1)):
                return False
            mappingST[c1] = c2
            mappingTS[c2] = c1

        
        return True
                
