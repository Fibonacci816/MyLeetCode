class Solution:
    # 记录包含零元素的行和列
    # 时间O(mn) 空间O(m+n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for row in zero_rows:
            matrix[row] = [0] * n
        for col in zero_cols:
            for row in range(m):
                matrix[row][col] = 0

    # 以第一行和第一列为标志位（重叠位置(0, 0)只能记录一个值，因此需要额外一个标志位），标记对应的列和行是否含零元素
    # 时间O(mn) 空间O(1)
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag = False  # 记录第一列是否有0
        # 第一行和第一列为标志位
        for i in range(m):
            if matrix[i][0] == 0:
                flag = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # 根据标志位置零
        # 列（不包括第一列）置零
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # 行置零
        for i in range(m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        # 第一列置零
        if flag:
            for i in range(m):
                matrix[i][0] = 0