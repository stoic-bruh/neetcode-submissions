class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res =[]
        for i in numbers:
            if (target - i) in numbers and (target-i)>i:
                res.append(numbers.index(i)+1)
                res.append(numbers.index(target-i)+1)
            else:
                continue
                
        return res
        