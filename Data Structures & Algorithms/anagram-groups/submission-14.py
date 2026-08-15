class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        for i in strs:
            if [sorted(i)] not in out:
                out.append([sorted(i)])
                
        for i in strs:
            for j in out:
                if j[0]==sorted(i):
                    j.append(i)
            
        for k in out:
            k.pop(0)
        return out

        
