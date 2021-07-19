class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        if n == 1:
            return [s]
        res = []
        visited = set() # 记录以某字符开头的字母排列是否已经得到
        for i in range(n):
            if s[i] not in visited:
                tmp = self.permutation(s[:i] + s[i+1:])
                res.extend([s[i] + sub_prem for sub_prem in tmp])
                visited.add(s[i])
        return res
