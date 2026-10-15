class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}                          # empty prefix, seen once

        for x in nums:
            prefix += x
            count += seen.get(prefix - k, 0)   # earlier prefixes that complete a sum of k
            seen[prefix] = seen.get(prefix, 0) + 1   # record current prefix AFTER the lookup

        return count