class Solution:
    # dp
    # 时间O(n) 空间O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sale = -inf, 0
        for price in prices:
            buy, sale = max(buy, sale - price), max(sale, buy + price - fee)  # fee的花费可以在买股票时也可以在买股票时，这里在卖股票时
        return sale

    # 贪心
    # 时间O(n) 空间O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[0] + fee  # 在买股票时计算fee的花费
        profit = 0
        for price in prices[1:]:
            if price + fee < buy:  # 股票价格+fee仍比当前持有的股票价格（可能包含fee）低，就在当前时间买入
                buy = price + fee
            elif price > buy:  # 暂时有利可图
                profit += price - buy
                buy = price  # 不计算fee，此时并不一定真的卖出股票（当第二天股票价格满足第一个条件时真的卖出，再计算fee），如果后来股票价格上升再卖利更大
        return profit