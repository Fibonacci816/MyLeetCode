class Solution:
    # 二分查找
    # 时间O(mlog(mn)) 空间O(1)
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))