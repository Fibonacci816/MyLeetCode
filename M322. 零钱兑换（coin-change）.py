class Solution:
    # dfs（自上而下递归）
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_coin = min(coins)
        @lru_cache(amount)
        def dfs(amount):
            if amount < self.min_coin:
                if amount == 0:
                    return 0
                return -1
            res = 1e5
            for coin in coins:
                cnt = dfs(amount-coin)
                if cnt >= 0 and cnt < res:
                    res = cnt + 1
            return res if res < 1e5 else -1
        return dfs(amount)
    #dp（自下而上迭代）
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [sys.maxsize] * (amount + 1)
        res[0] = 0
        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount >= coin:
                    res[cur_amount] = min(res[cur_amount-coin] + 1, res[cur_amount])
        return -1 if res[amount] == sys.maxsize else res[amount]
            