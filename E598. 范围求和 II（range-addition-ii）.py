class Solution:
    # 即求最小操作区域面积
    # 时间O(len(ops)) 空间O(1)
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_col = m, n
        for row, col in ops:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
        return min_row * min_col
