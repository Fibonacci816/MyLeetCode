class Solution:
    # 计数
    # 时间O(l+m+n)，其中l为indices长度； 空间O(m+n)
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        # return sum((row + col) & 1 for row in rows for col in cols)
        oddx = sum(row & 1 for row in rows)
        oddy = sum(col & 1 for col in cols)
        return oddx * (n - oddy) + (m - oddx) * oddy
