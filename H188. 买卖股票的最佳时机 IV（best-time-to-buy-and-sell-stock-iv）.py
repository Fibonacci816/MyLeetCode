class Solution:
    # dp
    # 时间O(nk) 空间O(k)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(k, len(prices) // 2)
        if not k:
            return 0
        buy = [-prices[0]] * k
        sell = [0] * k
        for price in prices[1:]:
            for i in range(k):
                buy[i], sell[i] = max(buy[i], (sell[i-1] if i > 0 else 0) - price), max(sell[i], buy[i] + price)
        return sell[-1]