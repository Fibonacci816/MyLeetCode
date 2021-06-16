class Solution:
    # dfs回溯法（时间复杂度极高）
    def __init__(self):
        self.move = [(0, 1), (1, 0)]
        self.res = float('inf')

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for i in range(m)]
        

        def vaild(x, y):
            return x < m and y < n and not visited[x][y]

        def dfs(x, y, dist):
            dist += grid[x][y]
            visited[x][y] = 1
            if (x, y) == (m-1, n-1):
                self.res = min(self.res, dist)
            for dx, dy in self.move:
                new_x, new_y = x + dx, y + dy
                if vaild(new_x, new_y):
                    dfs(new_x, new_y, dist)
            visited[x][y] = 0

        dfs(0, 0, 0)
        return self.res
    # 自顶向下递归
    def minPathSum1(self, grid: List[List[int]]) -> int:
        @lru_cache()
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i == 0:
                return dp(i, j-1) + grid[i][j]
            if j == 0:
                return dp(i-1, j) + grid[i][j]
            return min(
                dp(i-1, j) + grid[i][j],
                dp(i, j-1) + grid[i][j]
            )
        m, n = len(grid), len(grid[0])
        return dp(m-1, n-1)

    # 自底向上迭代（动态规划）
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i != 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                if j != 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
        return dp[m-1][n-1]

    # 自底向上迭代（动态规划）+空间压缩
    def minPathSum3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [inf] * n
        for i in range(m):
            for j in range(n):
                if j == 0 and i == 0:
                    dp[0] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[n-1]

    # dijkstra求最短路径（在此例中此算法时间复杂度高）
    def minPathSum4(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for i in range(m)]
        dist = [[float('inf')] * n for i in range(m)]
        def find_min():
            min_dist = float('inf')
            min_idx = None
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and min_dist > dist[i][j]:
                        min_dist = dist[i][j]
                        min_idx = (i, j)
            return min_idx
        
        def vaild(x, y):
            return x < m and y < n and not visited[x][y]

        move = [(1, 0), (0, 1)]
        def dijkstra():
            dist[0][0] = grid[0][0]
            while True:
                min_idx = find_min()
                if min_idx is None or min_idx == (m-1, n-1):
                    break
                x, y = min_idx
                visited[x][y] = 1
                for dx, dy in move:
                    new_x, new_y = x + dx, y + dy
                    if vaild(new_x, new_y) and dist[new_x][new_y] > dist[x][y] + grid[new_x][new_y]:
                        dist[new_x][new_y] = dist[x][y] + grid[new_x][new_y]
        
        dijkstra()
        return dist[m-1][n-1]
