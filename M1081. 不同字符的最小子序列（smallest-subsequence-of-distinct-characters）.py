class Solution:
    # 贪心 + 单调栈
    # 时间O(n) 空间O(nunique(s))
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        visited = set()
        res = []
        for ch in s:
            if ch not in visited:
                while res and res[-1] > ch and count[res[-1]] > 0:
                    visited.discard(res.pop())
                res.append(ch)
                visited.add(ch)
            count[ch] -= 1
        return ''.join(res)
