class Solution:
    # 贪心算法
    # 时间O(n) 空间O(n)
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)  # 字符计数
        res = []
        tmp = ''  # 满足条件的当前子串
        have_next = set()  # 当前子串中后面还会出现的字符
        for c in s:
            tmp += c
            count[c] -= 1
            if count[c] > 0:
                have_next.add(c)
            else:
                have_next.discard(c)
            if not have_next:
                res.append(len(tmp))
                tmp = ''
        return res
