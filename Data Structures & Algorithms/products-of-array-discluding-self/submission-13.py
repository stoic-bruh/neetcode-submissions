class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out =[]
        ot = 1
        pot = 1
        cunz = 0
        for i in range(len(nums)):
            if int(nums[i])==0:
                pot = 0
                cunz+=1
            else:
                ot *= int(nums[i])
        for i in range(len(nums)):
            if cunz>1:
                for k in range(len(nums)):
                    out.append(0)
                return out
                break
            elif int(nums[i])==0:
                nit = ot
                out.append(str(ot))
                continue
            else:
                if pot == 0 or ot == 0:
                    nit = 0 
                else:
                    nit = ot//int(nums[i])
            out.append(str(nit))
        return out