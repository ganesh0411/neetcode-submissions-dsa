class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i,j = 0, len(heights)-1
        maxWaterCapacity = 0

        while i < j:
            minHeight = min(heights[i], heights[j])
            maxWaterCapacity = max(maxWaterCapacity, (j - i) * minHeight)

            if minHeight == heights[i] :
                i += 1 
            elif minHeight == heights[j] :
                j -= 1
        
        return maxWaterCapacity

