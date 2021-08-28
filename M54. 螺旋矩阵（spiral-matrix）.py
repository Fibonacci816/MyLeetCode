class Solution:
	# 时间O(mn) 空间O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix[:] = list(zip(*matrix[1:]))[::-1]
        return res
