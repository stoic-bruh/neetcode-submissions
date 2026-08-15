class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cont_s = {}
        cont_t = {}
        for i in s:
            cont_s[i] = cont_s.get(i,0)+1
        for j in t:
            cont_t[j] = cont_t.get(j,0)+1
        return cont_t==cont_s
        