class Solution:
    # 哈希表
    # 时间O(n) 空间O(d)（d为文件最大深度）
    def lengthLongestPath(self, input: str) -> int:
        m = {-1: 0}
        ans = 0
        for path in input.split('\n'):
            depth = path.count('\t')
            m[depth] = m[depth-1] + len(path) - depth
            if '.' in path:
                ans = max(ans, m[depth]+depth)
        return ans