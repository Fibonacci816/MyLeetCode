class Solution:
	# dp
    # 时间O(N×M) 空间O(N×M)空间压缩O(min(N,M))
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * n2 for i in range(n1)]
        res = 0
        for i in range(n1):
            for j in range(n2):
                dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[i][j])
        return res
        """
        # 以下为空间压缩的dp
        ## 找较短的数组，可以进一步降低空间占用，非必须
        # if n1 < n2:
        #     nums1, nums2 = nums2, nums1
        #     n1, n2 = n2, n1
        dp = [0] * n2
        res = 0
        for i in range(n1):
            for j in range(n2-1, -1, -1):
                dp[j] = (dp[j-1] if i > 0 and j > 0 else 0) + 1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[j])
                if res == n2:  # 剪枝
                    return n2
        return res
        """
    # 滑动窗口（枚举两数组的对齐方式）
    # 时间O((N+M)×min(N,M)) 空间O(1)
    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        # 在某种对齐方式下得到最长公共子数组长度
        def max_len(l1, l2, max_l):
            res = 0
            commom_l = 0
            for i in range(max_l):
                commom_l = commom_l + 1 if nums1[l1+i] == nums2[l2+i] else 0
                res = max(res, commom_l)
            return res

        res = 0
        # 枚举 A 和 B 所有的对齐方式。对齐的方式有两类：
        # B 的首元素与 A 中的某个元素对齐
        for i in range(n1):
            max_l = min(n1-i, n2)
            if res >= max_l: break
            l = max_len(i, 0, max_l)
            res = max(res, l)
        # A 的首元素与 B 中的某个元素对齐
        for i in range(n2):
            max_l = min(n1, n2-i)
            if res >= max_l: break
            l = max_len(0, i, max_l)
            res = max(res, l)
        return res