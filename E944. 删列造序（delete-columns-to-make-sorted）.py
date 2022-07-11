class Solution:
    # 按列遍历
    # 时间O(mn) 空间O(1)
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            for i in range(1, len(col)):
                if col[i] < col[i-1]:
                    ans += 1
                    break
        return ans

    # 简化代码
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(col[i] < col[i-1] for i in range(1, len(col))) for col in zip(*strs))