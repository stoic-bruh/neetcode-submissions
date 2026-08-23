class Solution:
    def search(self, nums: nums[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            
            if nums[l]== target:
                return l
            elif nums[r] == target:
                return r
            elif l == (l+r)//2:
                break
            elif l == (l+r)//2:
                break
            elif nums[(l+r)//2] > target:
                r = (l+r)//2
            elif nums[(l+r)//2] < target:
                l = (l+r)//2
            else:
                return (l+r)//2
        return -1
        