class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_cnt = 0

        for num in nums:
            if num == 0:
                zero_cnt = zero_cnt+1
            else:
                product = product * num
        
        if zero_cnt > 1 : return [0] * len(nums)

        output = [0] * len(nums)
        for i in range(len(nums)):
            if zero_cnt == 1 and nums[i] != 0:
                output[i] = 0
            elif zero_cnt == 1 and nums[i] == 0:
                output[i] = product
            else:
                 output[i] = product//nums[i]

        
        return output