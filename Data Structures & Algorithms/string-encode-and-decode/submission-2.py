class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            for ch in i:
                s+=str(ord(ch))
                s+="."
            s+="/"
        return s


    def decode(self, s: str) -> List[str]:
        result = s.split("/")
        supersult = [ch.split(".") for ch in result]
        for i in supersult:
            i.pop()
        supersult.pop()
        out = []
        for k in supersult:
            p=""
            for l in k:
                p+=chr(int(l))
                
            out.append(p)
        
        return out
