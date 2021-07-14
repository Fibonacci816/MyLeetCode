class Solution(object):
    # 滑动窗口
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}  # 记录字符最后一次出现的位置
        n = len(s)
        left = -1
        res = 0
        for right in range(n):  # 移动窗口右侧
            if s[right] in visited:
                left = max(left, visited[s[right]])  # 移动窗口左侧
            res = max(res, right - left)
            visited[s[right]] = right
        return res
