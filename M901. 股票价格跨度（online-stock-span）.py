class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
        self.days = 0

    # 单调栈
    def next(self, price: int) -> int:
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        ans = self.days - (self.stack[-1] if self.stack else -1)
        self.prices.append(price)
        self.stack.append(self.days)
        self.days += 1
        return ans



class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1  # 股票价格小于或等于今天价格的最大连续日数股票价格小于或等于今天价格的最大连续日数
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append([price, weight])
        return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)