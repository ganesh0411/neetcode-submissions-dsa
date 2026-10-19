class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # i = 0

        # for num1 in nums1:
        #     for index, num2 in enumerate(nums2):
        #         if num1 == num2:
        #             i = index
        #             break
            
        #     j=i+1
        #     while j <= len(nums2)-1:
        #         if nums2[j] > num1:
        #             result.append(nums2[j])
        #             found = 1
        #             break
        #         else:
        #             j += 1
        #     else:
        #         result.append(-1)
        # return result

        next_greater = {}
        waiting = []

        for num in nums2:
            while waiting and num > waiting[-1]:
                next_greater[waiting.pop()] = num
            waiting.append(num)

        return [next_greater.get(num, -1) for num in nums1]










