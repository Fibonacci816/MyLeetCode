class Solution:
    # dfs
    # 时间O(mn) 空间O(mn)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        to_pad, no_pad = set(), set()

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and not visited[x][y] and board[x][y] == 'O'

        def dfs(x, y):
            if not is_valid(x, y):
                return
            visited[x][y] = 1
            no_pad.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    to_pad.add((x, y))
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    dfs(x, y)

        for x, y in to_pad - no_pad:
            board[x][y] = 'X'
        