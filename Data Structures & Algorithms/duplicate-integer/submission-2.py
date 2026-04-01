class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums :
            if num not in dict :
                dict[num] = 1
            elif num in dict :
                return True
        
        return False

