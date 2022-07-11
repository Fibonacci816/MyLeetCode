class Solution:
    # dp
    # 时间O(n) 空间O(1)
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = -prices[0], 0 , -prices[0], 0
        for price in prices[1:]:
            buy1, sell1 = max(buy1, -price), max(sell1, buy1 + price)
            buy2, sell2 = max(buy2, sell1 - price), max(sell2, buy2 + price)
        return sell2