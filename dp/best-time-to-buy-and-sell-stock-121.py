class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = prices[0], 0
        for i in range(1, len(prices)):
            if (p := prices[i]-minPrice) > maxProfit:
                maxProfit = p
            if prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit
