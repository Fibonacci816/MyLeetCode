class Solution:
    # dfs
    # 时间O(n^2) 空间O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * len(isConnected)
        def dfs(root):
            visited[root] = 1
            for node in range(n):
                if isConnected[root][node] and not visited[node]:
                    dfs(node)
        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        return ans