class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i = 0

        for num1 in nums1:
            for index, num2 in enumerate(nums2):
                if num1 == num2:
                    i = index
                    break
            
            j=i+1
            found = 0
            while j <= len(nums2)-1:
                if nums2[j] > num1:
                    result.append(nums2[j])
                    found = 1
                    break
                else:
                    j += 1
            else:
                result.append(-1)
        return result