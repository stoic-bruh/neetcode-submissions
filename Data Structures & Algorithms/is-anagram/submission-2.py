class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cont = []
        for i in s:
            cont.append(i)
        for j in t:
            if j in cont:
                cont.remove(j)
        
        if len(cont)==0:
            return True
        else :
            return False
        