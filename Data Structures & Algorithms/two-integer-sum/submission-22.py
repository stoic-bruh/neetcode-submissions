class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cont = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in cont:
                return [cont[complement], i]

            cont[num] = i