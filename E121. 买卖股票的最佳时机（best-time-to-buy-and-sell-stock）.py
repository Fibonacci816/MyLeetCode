class Solution(object):
    # 其实就是求最大连续差分子数列和
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = s = 0
        for i in range(1, len(prices)):
            s += prices[i] - prices[i-1]
            # 当前和一旦小于0，则清零，表示寻找新的连续子数列
            if s <= 0:
                s = 0
            else:
                res = max(res, s) 
        return res

    # 记录历史最小价格，求当前价格和历史低价的差值与历史最大利润作比较
    def maxProfit(self, prices):
        ans, min_price = 0, inf
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans