class Solution:
    # 回溯
    # 时间O(4^n) 空间O(n)
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4:
            return False
        edge_len = total_len // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > edge_len:
            return False
        edges = [0] * 4
        
        def dfs(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= edge_len and dfs(idx+1):
                    return True
                edges[i] -= matchsticks[idx]
            return False

        return dfs(0)
        
    # dp
    # 时间O(n × 2^n) 空间O(2^n)
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4:
            return False
        edge_len = total_len // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > edge_len:
            return False
        
        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(len(matchsticks)):
                if i & 1 << j == 0:
                    continue
                pre = i & ~(1 << j)
                if dp[pre] >= 0 and dp[pre] + matchsticks[j] <= edge_len:
                    dp[i] = (dp[pre] + matchsticks[j]) % edge_len
                    break

        return dp[-1] == 0
        
