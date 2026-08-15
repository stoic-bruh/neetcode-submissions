class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        buff = []
        for row in board:
            for i in row:
                if i == ".":
                    continue
                if row.count(i)>1:
                    return False
               
           
        
        for i in range(9):
            for k in range(9):
                buff.append(board[k][i])
            for l in buff:
                if l ==".":
                    continue
                if buff.count(l)>1:
                    return False
                
            buff = []
        
        for r in range(0,9,3):
            for s in range(0,9,3):
                box = []
                for i in range(r,r+3):
                    for j in range(s,s+3):
                        box.append(board[i][j])

                for  i in box:
                    if i ==".":
                        continue
                    if box.count(i)>1:
                        return False
        return True
        


        
