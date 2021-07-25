class Solution:
    # 归并
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(str1, str2):
            n = min(len(str1), len(str2))
            end = 0
            while end < n and str1[end] == str2[end]:
                end += 1
            return str1[:end]
        
        while (n := len(strs)) > 1:
            res = []
            # 两两归并
            for i in range(0, n, 2):
                if i + 2 > n:
                    res.append(strs[i])
                else:
                    res.append(common_prefix(strs[i], strs[i+1]))
            strs = res
        return strs[0]
    
    # 逐位置判断是否所有字符串在相同位置的字符都相同
    # 如果在第i位判断为False，则返回任意字符串的前i位（不包括第i位）            
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        min_l = 200
        for s in strs:
            l = len(s)
            if l < min_l:
                min_l = l
        max_idx = 0
        for i in range(min_l):
            chrs = set()
            for s in strs:
                chrs.add(s[i])
            if len(chrs) > 1:
                break
            max_idx = i + 1       
        return strs[0][:max_idx]
    
    # 对所有字符串排序，排序后第一个字符串和最后一个字符串的最长公共前缀即为所求
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        start_str, end_str = strs[0], strs[-1]
        min_l = len(start_str)
        for i in range(min_l):
            if start_str[i] != end_str[i]:
                return start_str[:i]
        return start_str