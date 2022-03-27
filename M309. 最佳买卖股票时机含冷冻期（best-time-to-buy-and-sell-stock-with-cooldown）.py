class Solution:
    # dp（三个状态）
    # 时间O(n) 空间O(1)
    def maxProfit(self, prices: List[int]) -> int:
        buy, sale_cooldown, sale = -inf, 0, 0  # 持有股票，卖出股票进入冷冻期，不持有股票
        for price in prices:
            buy, sale_cooldown, sale = max(buy, sale - price), buy + price, max(sale, sale_cooldown)
        return max(sale_cooldown, sale)