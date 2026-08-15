class Solution:
    def trap(self, height: List[int]) -> int:
        wat = 0
        for i in range(len(height)):
            if i ==0:
                lef=0
                righ = sorted(height[i:])[-1]
            elif i==len(height)-1:
                righ =0
                lef = sorted(height[:i])[-1]
            else:
                lef = sorted(height[:i])[-1]
                righ = sorted(height[i:])[-1]
            wat += max(min(lef,righ)-height[i],0)
        return wat
        