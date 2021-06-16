class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:   
        m, n = len(matrix), len(matrix[0])
        max_side = 0
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '1':
                    if i== 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(
                            matrix[i-1][j-1], 
                            matrix[i-1][j], 
                            matrix[i][j-1]
                        ) + 1
                else:
                    matrix[i][j] = 0
                max_side = max(max_side, matrix[i][j])
        return max_side * max_side
