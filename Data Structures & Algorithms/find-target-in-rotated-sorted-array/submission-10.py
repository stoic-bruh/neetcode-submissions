class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid =(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                if nums[l]>target and nums[mid]>=nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            if nums[mid]<target:
                if nums[r]<target and nums[r]>nums[mid]:
                    r=mid-1
                else:
                    l = mid+1
        if nums[mid]==target:
            return mid    
        else:
            return -1
        