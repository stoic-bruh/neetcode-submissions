class MinStack:

    def __init__(self):
        self.stk = []
        self.minu = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minu)==0:
            self.minu.append(val)
        else:
            self.minu.append(min(self.minu[-1],val))

    def pop(self) -> None:
        self.stk.pop(-1)
        
        self.minu.pop(-1)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minu[-1]

        
