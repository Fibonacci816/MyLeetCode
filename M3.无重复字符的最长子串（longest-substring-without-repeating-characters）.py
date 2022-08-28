class Solution:
    # 滑动窗口 + 哈希表
    # 时间O(n) 空间O(V)，V为字符集大小
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        ans, l = 0, -1
        for i, c in enumerate(s):
            if c in visited:
                l = max(l, visited[c])
            ans = max(ans, i - l)
            visited[c] = i
        return ans
