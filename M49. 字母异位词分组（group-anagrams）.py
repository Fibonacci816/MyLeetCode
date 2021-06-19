class Solution:
	# 字符串排序后相等的为一组
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
        return list(res.values())