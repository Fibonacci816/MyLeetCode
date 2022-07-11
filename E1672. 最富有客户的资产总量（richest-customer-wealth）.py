class Solution:
    # 遍历
    # 时间O(mn) 空间O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))