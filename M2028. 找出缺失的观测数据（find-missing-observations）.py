class Solution:
    # 时间O(m+n) 空间O(1)
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        target_sum = mean * (m + n) - sum(rolls)
        if 1 * n <= target_sum <= 6 * n:
            q, r = divmod(target_sum, n)
            return [q] * (n - r) + [q + 1] * r
        return []
