class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        low, high = 0, len(nums)        # high is exclusive
        while low < high:               # < because low == high means empty
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid              # not mid - 1, since high is exclusive
            else:
                return mid
        return -1        # first index with nums[index] >= target
