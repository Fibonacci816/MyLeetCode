class Solution:
    # 遍历每个子序列，判断子序列时候仅包含元音且包含全部元音
    # 时间O(n^2) 空间O(1)
    def countVowelSubstrings(self, word: str) -> int:
        metas = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        cnt = 0
        for start in range(n-4):
            if word[start] not in metas:
                continue
            tmp = {word[start]}
            for end in range(start + 1, n):
                if word[end] not in metas:
                    break
                tmp.add(word[end])
                if len(tmp) == len(metas):
                    cnt += 1
        return cnt
    
    # 和上面的方法思路大致相同，没有剪枝，比较花哨的写法
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        return sum(set(word[i: j + 1]) == set('aeiou') for i in range(n) for j in range(i + 1, n))
        