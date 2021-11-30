class Solution:
	# 时间O(mn) 空间O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix[:] = list(zip(*matrix[1:]))[::-1]
        return res

    # 时间O(mn) 空间O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        for start in range(m//2):
        for i in range(start, n-start-1):
          res.append(matrix[start][i])
        for i in range(start, m-start-1):
          res.append(matrix[i][n-1-start])
        for i in range(n-start-1, start, -1):
          res.append(matrix[m-start-1][i])
        for i in range(m-start-1, start, -1):
          res.append(matrix[i][start])
        return res
