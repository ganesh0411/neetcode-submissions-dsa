class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #O(n) regular Solution
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index

        #O(log n) solution using Binary search

        l, r = 0, len(nums) - 1

        while l <= r:                                   # CHANGED: <=
            mid = (l + r) // 2

            if nums[mid] == target:                     # CHANGED: equality first
                return mid

            if nums[l] <= nums[mid]:                    # ADDED: left half is sorted
                if nums[l] <= target < nums[mid]:       #   target inside the left half
                    r = mid - 1
                else:
                    l = mid + 1
            else:                                       # ADDED: right half is sorted
                if nums[mid] < target <= nums[r]:       #   target inside the right half
                    l = mid + 1
                else:
                    r = mid - 1

        return -1