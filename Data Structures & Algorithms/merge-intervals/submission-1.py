class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []

        intervals.sort()
        result = []
        i = 1
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            resTotal = len(result)
            if intervals[i][0] <= result[resTotal - 1][1]:
                result[-1][1] = max(intervals[i][1], result[resTotal - 1][1])
            else : 
                result.append(intervals[i])
        
        return result

print(Solution().merge([[1,3],[2,6],[7,8]]))   # happy:     [[1,6],[7,8]]
print(Solution().merge([[2,6],[1,4],[6,7]]))   # unsorted:  [[1,7]]
print(Solution().merge([[1,2],[5,6],[9,10]]))  # no merge:  [[1,2],[5,6],[9,10]]
print(Solution().merge([[1,4]]))               # single:    [[1,4]]
print(Solution().merge([]))                    # empty:     []





