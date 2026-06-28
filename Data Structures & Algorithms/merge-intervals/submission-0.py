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

