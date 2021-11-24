class Solution:
    # 根据字母在每个数字中出现的次数
    # 时间O(n) 空间10+26
    def originalDigits(self, s: str) -> str:
        char_cnt = Counter(s)
        num_cnt = [0] * 10
        num_cnt[0] = char_cnt['z']
        num_cnt[2] = char_cnt['w']
        num_cnt[4] = char_cnt['u']
        num_cnt[6] = char_cnt['x']
        num_cnt[8] = char_cnt['g']
        num_cnt[3] = char_cnt['h'] - num_cnt[8]
        num_cnt[5] = char_cnt['f'] - num_cnt[4]
        num_cnt[7] = char_cnt['v'] - num_cnt[5]
        num_cnt[1] = char_cnt['o'] - num_cnt[0] - num_cnt[2] - num_cnt[4]
        num_cnt[9] = (char_cnt['n'] - num_cnt[1] - num_cnt[7]) // 2
        return ''.join(str(i) * num_cnt[i] for i in range(10))
