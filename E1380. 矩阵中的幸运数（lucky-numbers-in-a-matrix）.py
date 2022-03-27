class Solution:
    # 时间O(mn) 空间O(m+n)
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if max_col[j] <= matrix[i][j] <= min_row[i]]