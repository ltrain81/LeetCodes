class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        result = 0
        while right < n:
            currentProfit = prices[right] - prices[left]
            if currentProfit > 0:
                result = max(result, currentProfit)
            else:
                left = right
            right += 1
        
        return result
            
            
            
