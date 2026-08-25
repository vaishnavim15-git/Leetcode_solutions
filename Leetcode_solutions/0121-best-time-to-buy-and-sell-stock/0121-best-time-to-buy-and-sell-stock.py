class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        n=len(prices)
        for i in range(0,n):
            min_price=min(prices[i],min_price)
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit
solution=Solution()    
print(solution.maxProfit([7,6,4,3,1]))        