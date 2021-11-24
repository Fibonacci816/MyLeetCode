class Solution:
    # 先记录每一个不相同的位置再进行判断
    # 时间O(n) 空间O(n)
    def buddyStrings(self, s: str, goal: str) -> bool:
        n1, n2 = len(s), len(goal)
        if n1 != n2 or n1 < 2:  # 因为n < 2的情况包含在最后的判断里，也可以不加
            return False
        diff = [(s[i], goal[i]) for i in range(n1) if s[i] != goal[i]]
        return len(diff) == 0 and len(set(s)) != n1 or len(diff) == 2 and diff[0] == diff[1][::-1]