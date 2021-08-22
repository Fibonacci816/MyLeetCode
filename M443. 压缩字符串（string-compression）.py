class Solution:
    # 逐位读取计数，判断和前一位字符是否相同
    # 时间O(n) 空间O(1)
    def compress(self, chars: List[str]) -> int:
        def get_cnt_len(cnt):
            if cnt == 1:
                return 0
            else:
                return len(str(cnt))

        chars += ['~']  # 尾部添加一个不会出现在字符数组中的字符，这样不需要特殊处理遍历到最后一位的情况
        res = 0
        pre = chars[0]
        cnt = 1
        for ch in chars[1:]:
            if ch == pre:
                cnt += 1
            else:
                chars[res] = pre
                cnt_len = get_cnt_len(cnt)
                if cnt_len > 0:
                    chars[res+1:res+1+cnt_len] = [ch for ch in str(cnt)]
                res += cnt_len + 1
                cnt = 1
            pre = ch
        chars = chars[:res]
        return res
        