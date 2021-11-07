class Solution:
    # dp（存储用字典）
    # 时间O(n) 空间O(n)
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())
