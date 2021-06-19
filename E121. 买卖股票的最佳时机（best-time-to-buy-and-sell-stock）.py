class Solution(object):
    # 其实就是求最大连续子数列和
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        res = s = 0
        for i in range(1, n):
            s += prices[i] - prices[i-1]
            # 当前和一旦小于0，则清零，表示寻找新的连续子数列
            if s <= 0:
                s = 0
            else:
                res = max(res, s) 
        return res

    # 记录历史最小价格，求当前价格和历史低价的差值
    def maxProfit(self, prices):
        min_price = prices[0]
        res = 0
        for price in prices[1:]:
            if min_price > price:
                min_price = price
            else:
                res = max(res, price-min_price)
        return res