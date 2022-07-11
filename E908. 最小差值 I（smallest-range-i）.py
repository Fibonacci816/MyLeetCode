class Solution:
    # 时间O(n) 空间O(1)
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)