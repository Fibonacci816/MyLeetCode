class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        area = [0]
        
        def isvalid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y]

        def dfs(x, y):
            grid[x][y] = 0
            area[0] = area[0] + 1
            for dx, dy in moves:
                if isvalid(x+dx, y+dy):
                    dfs(x+dx, y+dy)
        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    area = [0]
                    dfs(x, y)
                    max_area = max(max_area, area[0])
        return max_area