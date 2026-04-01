class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums);
        i = 0
        j = 1
        while j <= len(sortedNums) - 1 :
            if (sortedNums[i] == sortedNums[j]) : 
                return True  
            i = i + 1
            j = j + 1
        return False
