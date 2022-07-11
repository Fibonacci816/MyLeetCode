class Solution:
    # 遍历
    # 时间O(n) 空间O(1)
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l, cnt = 1, 0
        for c in s:
            w = widths[ord(c)-ord('a')]
            cnt += w
            if cnt > 100:
                l += 1
                cnt = w
        return [l, cnt]