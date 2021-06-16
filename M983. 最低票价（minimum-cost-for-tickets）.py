class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache()
        def dp(i):
            if i > days[-1]:
                return 0
            if i not in days:
                 return dp(i+1)
            return min(
                dp(i+1) + costs[0],
                dp(i+7) + costs[1],
                dp(i+30) + costs[2]
            )
        return dp(1)