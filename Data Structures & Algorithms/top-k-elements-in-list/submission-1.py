class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freqMap = {}

        for num in nums :
            if num not in freqMap :
                freqMap[num] = 1
            elif num in freqMap:
                freqMap[num] = freqMap[num] + 1

        sortedMaps = sorted(freqMap.items(),key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sortedMaps[i][0])

        return result
