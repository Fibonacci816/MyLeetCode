class Solution:
    # 两次遍历
    # 时间O(n) 空间O(1)
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = []
        pre_idx = -n
        for i, _c in enumerate(s):
            if _c == c:
                pre_idx = i
            ans.append(i-pre_idx)
        next_idx = 2 * n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                next_idx = i
            ans[i] = min(ans[i], next_idx-i)
        return ans