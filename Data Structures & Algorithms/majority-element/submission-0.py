class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqTable = defaultdict()
        for num in nums:
            if num not in freqTable:
                freqTable[num]=1
            else:
                freqTable[num] += 1
        sorted_items = sorted(freqTable.items(), key=lambda item: item[1], reverse=True)
        return sorted_items[0][0]
        