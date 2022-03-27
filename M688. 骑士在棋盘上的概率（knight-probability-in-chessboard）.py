class Solution:
    def __init__(self):
        self.can_move = [(i, j) for i in [-1, 1, -2, 2] for j in [-1, 1, -2, 2] if abs(i) != abs(j)]
        self.move_prob = 0.125
        self.ans = 0.0

    def is_valid(sellf, n, row, column):
        return 0 <= row < n and 0 <= column < n

    # 会超时
    def dfs(self, n, k, row, column, prob):
        for dx, dy in self.can_move:
            x, y = row + dx, column + dy
            if self.is_valid(n, x, y):
                cur_prob = prob * self.move_prob
                if k > 1:
                    self.dfs(n, k - 1, x, y, cur_prob)
                else:
                    self.ans += cur_prob
    
    # 每向外走一次都可以合并（相同位置概率相加）
    def bfs(self, n, k, row, column, prob):
        positions_and_probs = {(row, column): prob}
        for _ in range(k):
            new_positions_and_probs = defaultdict(float)
            for (row, column), prob in positions_and_probs.items():
                for dx, dy in self.can_move:
                    x, y = row + dx, column + dy
                    if self.is_valid(n, x, y):
                        new_positions_and_probs[(x, y)] += prob *self.move_prob
            positions_and_probs = new_positions_and_probs
        self.ans = sum(positions_and_probs.values())

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.prob_matrix = [[0] * n for _ in range(n)]
        self.k = k
        self.bfs(n, k, row, column, 1.0)

        return self.ans