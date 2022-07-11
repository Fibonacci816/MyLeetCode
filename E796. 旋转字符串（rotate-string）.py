class Solution:
    # 遍历判断
    # 时间O(n^2) 空间O(n)
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i, c in enumerate(s):
            if c == goal[0] and s[i:]+s[:i] == goal:
                return True
        return False

    # 搜索子串
    # 时间O(n) 空间O(n)
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
