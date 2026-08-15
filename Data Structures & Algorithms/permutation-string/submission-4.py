class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sebs = {}
        counts = {}
        for i in s1:
            sebs[i] = sebs.get(i,0)+1

        l=0
        r=len(s1)
        for k in range(r):
            counts[s2[k]] = counts.get(s2[k],0)+1




        while True:
            if counts == sebs:
                return True
                break
            if r == len(s2):
                break

            else:
                counts[s2[l]] = counts.get(s2[l],0)-1
                if counts[s2[l]] == 0:
                    del counts[s2[l]]
                l+=1
                counts[s2[r]] = counts.get(s2[r],0)+1
                r+=1
        return False
                
            
                