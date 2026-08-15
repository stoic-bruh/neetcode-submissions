class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 0
        for i in range(len(prices)):
            if prices[i] == max(prices):
                continue
            elif i == len(prices)-1:
                continue
            elif prices[i] == max(prices[i:]) :
                continue
            else:
                mn = max(mn,(max(prices[i:])-prices[i]))
        return mn
                

        