class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        def isvalid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == '1'

        def dfs(x, y):
            grid[x][y] = '0'
            for dx, dy in moves:
                if isvalid(x+dx, y+dy):
                    dfs(x+dx, y+dy)
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(x, y)
                    res += 1
        return res
