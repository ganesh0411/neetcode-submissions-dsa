class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)
            output = [1] * n

            prefix = 1
            for i in range(n):
                output[i] = prefix        # product of everything left of i
                prefix *= nums[i]

            suffix = 1
            for i in range(n - 1, -1, -1):
                output[i] *= suffix       # multiply in product of everything right of i
                suffix *= nums[i]

            return output