class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = 10001
        for p in prices:
            if prev < p:
                profit += p - prev
            prev = p
        
        return profit