class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
    
        for i in tokens:
            if i not in("+","-","*","/"):
                stk.append(i)
            elif i == "+":
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b+a)
            elif i == "-":
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b-a)
            elif i == "/":
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b/a)
            elif i == "*":
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b*a)
        
        return int(stk[0])



        