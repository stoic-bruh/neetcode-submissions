class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        ref = (j-i)*min(heights[i],heights[j])
        while i<=j:
            max = (j-i)*min(heights[i],heights[j])
            if max>=ref:
                ref=max
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return ref


        