class Solution:
    # 时间O(n^2) 空间O(1)
    def projectionArea(self, grid: List[List[int]]) -> int:
        area1 = area2 = area3 = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            _max = 0
            for j in range(n):
                if grid[i][j] != 0:
                    area1 += 1
                _max = max(_max, grid[i][j])
            area2 += _max
        for j in range(n):
            _max = 0
            for i in range(m):
                _max = max(_max, grid[i][j])
            area3 += _max
        return area1 + area2 + area3
    
    # 简化代码
    def projectionArea(self, grid: List[List[int]]) -> int:
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, grid))
        zxArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        return xyArea + yzArea + zxArea

