class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tbox = nums.copy()
        tbox.sort()
        out = []
        for i in nums:
            target = i*-1
            tbox.remove(i)
            j = 0
            k = -1
            while j-k != len(tbox):
                if tbox[j]+tbox[k] == target:
                    out.append([i,tbox[j],tbox[k]])
                    j+=1
                elif tbox[j]+tbox[k] > target:
                    k-=1
                else:
                    j+=1
            tbox.append(i)
            tbox.sort()
            
        for i in range(len(out)):
            out[i] = sorted(out[i])
        out = list(set(tuple(x) for x in out))
        return out
                    




        