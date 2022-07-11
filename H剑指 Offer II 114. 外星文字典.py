class Solution:
    # 拓扑排序
    def alienOrder(self, words: List[str]) -> str:
        char_set = set(''.join(words))
        n = len(words)
        links = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(1, n):
            for c1, c2 in zip(words[i-1], words[i]):
                if c1 != c2:
                    links[c1].append(c2)
                    in_degree[c2] += 1
                    break
            else:
                if len(words[i-1]) > len(words[i]):
                    return ""
                
        candidate = []
        for c in char_set:
            if in_degree[c] == 0:
                candidate.append(c)
        ans = ""
        while candidate:
            c = candidate.pop()
            ans += c
            char_set.remove(c)
            for _next in links[c]:
                in_degree[_next] -= 1
                if in_degree[_next] == 0:
                    candidate.append(_next)
        return "" if char_set else ans
