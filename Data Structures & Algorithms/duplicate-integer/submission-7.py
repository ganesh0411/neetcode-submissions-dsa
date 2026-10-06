class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # frequencyMap = {}

        # for num in nums:
        #     if num not in frequencyMap:
        #         frequencyMap[num] = 1;
        #     elif num in frequencyMap:
        #         return True;

        # return False

        numSet = set(nums);
        return len(nums) != len(numSet)
