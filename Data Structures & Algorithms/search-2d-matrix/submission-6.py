class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        if len(matrix)==0:
            return False
         
        while l<=r:
            mide = (l+r)//2
            arr=matrix[mide]
            if r<0:
                return False
            if arr[0]<=target and arr[-1]>=target:
                j = 0
                k = len(arr)-1
                while j<=k:
                    mid = (j+k)//2
                    if arr[mid]==target:
                        return True
                    elif arr[mid]<target:
                        j = mid+1
                    elif arr[mid]>target:
                        k = mid-1
                    
                return False
            elif arr[0]>target:
                r = mide-1 
            elif arr[-1]<target:
                l = mide+1 
            else:
                return False
        return False   



                


        