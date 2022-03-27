class Solution:
    # 贪心
    # 时间O(n) 空间O(1)（sum里面是iterator，所以这种写法隐含的空间复杂度为O(n)）
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

    # dp
    # 时间O(n) 空间O(1)
    def maxProfit(self, prices: List[int]) -> int:
        buy, sale = -inf, 0
        for price in prices:
            buy, sale = max(sale - price, buy), max(buy + price, sale)
        return sale