class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if a > 0:
#                 break

#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return res


        sortedNums = sorted(nums)

        p = 0
        result = []

        while p < len(sortedNums)-2:
            subTarget = -(sortedNums[p])
            q = p + 1
            r = len(sortedNums) - 1
            while q < r:
                subTotal = sortedNums[q] + sortedNums[r]
                if subTotal < subTarget:
                    q += 1
                elif subTotal > subTarget:
                    r -= 1
                else:
                    result.append([sortedNums[p], sortedNums[q], sortedNums[r]])
                    q += 1
                    r -= 1
            p += 1

        triplets = [list(t) for t in set(tuple(t) for t in result)]

        return triplets
