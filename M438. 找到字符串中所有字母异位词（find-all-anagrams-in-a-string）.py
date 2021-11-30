class Solution:
    # 滑动窗口，判断窗口包含的字符串是否为异位词
    # 时间O((len(s)-len(p))*k) 空间O(k) k为p的长度或26，和使用的比较函数is_same有关
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_same(s1, s2):
            return sorted(s1) == sorted(s2)
            # cnt1 = [0] * 26
            # cnt2 = [0] * 26
            # for c1, c2 in zip(s1, s2):
            #     cnt1[ord(c1)-ord('a')] += 1
            #     cnt2[ord(c2)-ord('a')] += 1
            # return cnt1 == cnt2

        ls, lp = len(s), len(p)
        res = []
        flag = False
        for i in range(ls-lp+1):
            if i == 0:
                flag = is_same(s[:lp], p)
            elif s[i-1] != s[i+lp-1]:
                flag = False if flag else is_same(s[i:i+lp], p)
            if flag:
                res.append(i)
        return res

    # 优化比较函数，维护两个字符计数数组，根据两个数组是否相同判断是否为异位词
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        if ls < lp:
            return []
        res = []
        cnt_s = [0] * 26
        cnt_p = [0] * 26
        for i in range(lp):
            cnt_s[ord(s[i])-ord('a')] += 1
            cnt_p[ord(p[i])-ord('a')] += 1
        flag = cnt_s == cnt_p
        if flag:
            res.append(0)
        for i in range(ls-lp):
            if s[i] != s[i+lp]:
                cnt_s[ord(s[i])-ord('a')] -= 1
                cnt_s[ord(s[i+lp])-ord('a')] += 1
                flag = False if flag else cnt_s == cnt_p
            if flag:
                res.append(i+1)
        return res