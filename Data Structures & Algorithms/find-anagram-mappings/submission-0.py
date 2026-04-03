class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        nums2Table = {}
        for index, num2 in enumerate(nums2):
            nums2Table[num2] = index

        result = []
        for num1 in nums1:
            result.append(nums2Table.get(num1))

        return result