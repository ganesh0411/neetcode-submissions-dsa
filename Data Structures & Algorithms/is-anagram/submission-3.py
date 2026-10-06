from collections import Counter


class Solution:

    def createFrequencyMap(self, strg: str)-> dict:
        freqMap = {}
        for s in strg:
            if s not in freqMap:
                freqMap[s] = 1;
            elif s in freqMap:
                freqMap[s] += 1;
        return freqMap;


    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t) :
        #     return True
        # else :
        #     return False

        # return Counter(s) == Counter(t)

        m1 = self.createFrequencyMap(s);
        m2 = self.createFrequencyMap(t);
        return m1 == m2



