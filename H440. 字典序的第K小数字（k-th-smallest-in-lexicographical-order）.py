class Solution:
    # dfs（十叉树）
    # 时间O(k) 空间O(k)
    def findKthNumber(self, n: int, k: int) -> int:
        rank = []
        def dfs(start, n, k):
            if start > n or len(rank) >= k:
                return
            rank.append(start)
            for i in range(10):
                dfs(start * 10 + i, n, k)
        for i in range(1, 10):
            dfs(i, n, k)
        return rank[-1]

    # 统计前缀
    # 时间O((logn)^2)（常数项为10） 空间O(1)
    def findKthNumber(self, n: int, k: int) -> int:
        # 相当于计算以prefix为根节点的十叉树节点总数
        def pre_count(prefix, n):
            prefix2 = prefix + 1
            count = 0
            while prefix <= n:
                count += min(n+1, prefix2) - prefix  # 十叉树每一层节点总数
                prefix *= 10
                prefix2 *= 10
            return count
        
        num, rank = 1, 1
        while rank < k:
            cnt = pre_count(num, n)
            if rank + cnt > k:
                num *= 10
                rank += 1
            else:
                rank += cnt
                num += 1
        return num



