from collections import Counter


class Solution:
    #SOLUTION 3
    def createFrequencyMap(self, strg: str)-> dict:
        freqMap = {}
        for s in strg:
            if s not in freqMap:
                freqMap[s] = 1;
            elif s in freqMap:
                freqMap[s] += 1;
        return freqMap;


    def isAnagram(self, s: str, t: str) -> bool:
        #SOLUTION 1
        # if sorted(s) == sorted(t) :
        #     return True
        # else :
        #     return False

        #SOLUTION 2
        # return Counter(s) == Counter(t)

        m1 = self.createFrequencyMap(s);
        m2 = self.createFrequencyMap(t);
        return m1 == m2



