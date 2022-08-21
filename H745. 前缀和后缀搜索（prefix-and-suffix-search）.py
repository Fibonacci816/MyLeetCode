class WordFilter:
    # 字典树
    # 时间O(n·l^2) 空间O(n·l^2)
    def __init__(self, words: List[str]):
        self.dict = {}
        for i, word in enumerate(words):
            l = len(word)
            cur = self.dict
            for j in range(l):
                tmp = cur
                for k in range(j, l):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[('#', '#')] = i
                tmp = cur
                for k in range(j, l):
                    key = ('#', word[-k-1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[('#', '#')] = i
                key = (word[j], word[-j-1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[('#', '#')] = i


    def f(self, pref: str, suff: str) -> int:
        ans = self.dict
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in ans:
                return -1
            ans = ans[key]
        return ans[('#', '#')]



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)