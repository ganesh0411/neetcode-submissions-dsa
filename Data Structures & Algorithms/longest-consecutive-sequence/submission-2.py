class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums);
        longestSequence = 0;
        for num in numsSet:
            if (num - 1) not in numsSet:
                sequenceLength = 1;
                while (num + sequenceLength) in numsSet:
                    sequenceLength += 1;
                longestSequence = max(sequenceLength, longestSequence);
        return longestSequence;
