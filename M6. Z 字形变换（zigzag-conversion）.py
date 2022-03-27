class Solution:
    # 时间O(n) 空间O(n)
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        ans = [[] for _ in range(min(n, numRows))]
        for i in range(n):
            rank = i % (2 * numRows - 2)
            row = rank if rank < numRows else (2 * numRows -2 - rank)
            ans[row].append(s[i])
        return ''.join(reduce(lambda x, y: x + y, ans))
