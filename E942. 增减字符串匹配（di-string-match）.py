class Solution:
    # 贪心
    # 时间O(n) 空间O(1)
    def diStringMatch(self, s: str) -> List[int]:
        start, end = 0, len(s)
        ans = []
        for c in s:
            if c == "I":
                ans.append(start)
                start += 1
            else:
                ans.append(end)
                end -= 1
        ans.append(start)
        return ans