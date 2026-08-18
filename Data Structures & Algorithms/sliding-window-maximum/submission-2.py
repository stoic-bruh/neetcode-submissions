class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxar = []
        maxi = nums[0]
        for i in range(k):
            if nums[i]>maxi:
                maxi = nums[i]
        maxar.append(maxi)
        l = 0
        r = k-1
        while r != len(nums)-1:
            if nums[l]< maxi:
                l = l+1
                r = r+1
                maxi = max(maxi,nums[r])
                maxar.append(maxi)
                continue
            elif nums[l]== maxi:
                l+=1
                r+=1
                maxi = nums[l]
                for i in range(l,r+1):
                    if nums[i]>maxi:
                        maxi = nums[i]
                maxar.append(maxi)
        return maxar
                



            
            
        