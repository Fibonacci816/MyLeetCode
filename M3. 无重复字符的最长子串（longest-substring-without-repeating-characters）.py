class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}
        n = len(s)
        left = -1
        res = 0
        for right in range(n):
            if s[right] in visited:
                left = max(left, visited[s[right]])
            res = max(res, right - left)
            visited[s[right]] = right
        return res
