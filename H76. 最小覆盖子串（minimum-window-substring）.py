class Solution:
    # 滑动窗口 + 计数
    # 时间O(n) 空间O(C) C=26
    def minWindow(self, s: str, t: str) -> str:
        t_cnt, s_cnt = Counter(t), defaultdict(int)
        t_unique, s_unique = len(t_cnt), 0
        l, ans = 0, ""
        for r, c in enumerate(s):
            s_cnt[c] += 1
            if c in t_cnt and s_cnt[c] == t_cnt[c]:
                s_unique += 1
                while s_unique == t_unique:
                    if ans == "" or len(ans) > r - l + 1:
                        ans = s[l:r+1]
                    if s[l] in t_cnt and s_cnt[s[l]] == t_cnt[s[l]]:
                        s_unique -= 1
                    s_cnt[s[l]] -= 1
                    l += 1
        return ans