class Solution:
    # 遍历一行，剩余部分转置并且逆序，重复上述操作直到剩余部分为空
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = list(zip(*matrix[1:]))[::-1]
        return res

    # 模拟，按四个方向进行循环遍历
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for i in range(m)]
        path = []

        def circle_order(start, direct):
            x, y = start
            if direct == 0:
                while y < n and not visited[x][y]:
                    path.append(matrix[x][y])
                    visited[x][y] = 1
                    y += 1
                y -= 1
                x += 1
            elif direct == 1:
                while x < m and not visited[x][y]:
                    path.append(matrix[x][y])
                    visited[x][y] = 1
                    x += 1
                x -= 1
                y -= 1
            elif direct == 2:
                while y >= 0 and not visited[x][y]:
                    path.append(matrix[x][y])
                    visited[x][y] = 1
                    y -= 1
                y += 1
                x -= 1
            elif direct == 3:
                while x >= 0 and not visited[x][y]:
                    path.append(matrix[x][y])
                    visited[x][y] = 1
                    x -= 1
                x += 1
                y += 1
            if len(path) < m*n:
                circle_order((x, y), (direct + 1) % 4)
            
        circle_order((0, 0), 0)
        return path
