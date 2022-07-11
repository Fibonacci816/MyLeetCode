class Solution:
    # 约瑟夫环 f(n, k) = (f(n-1, k) + k) % n ，从0开始编号
    # 递归
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (self.findTheWinner(n - 1, k) - 1 + k) % n + 1

    # 迭代
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(1, n):
            winner = (winner - 1 + k) % (i + 1) + 1
        return winner