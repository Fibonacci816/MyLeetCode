class Solution:
	# 枚举子集的和
    def canPartition(self, nums: List[int]) -> bool:
    	total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        ss = {0}  # 子集的和，初始化为{0}是为了得到只有一个元素的子集的和（即该元素的值）
        for num in nums:
            subs = {num + s for s in ss}  # 加入新的元素后，所有新增的子集的和
            if target in subs:
                return True
            ss |= subs
        return False

    # 动态规划
    def canPartition2(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ & 1 == 1:
            return False
        target = sum_ // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]  # dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        		if dp[target]:  # 剪枝，一旦已取元素构成的子集和等于target，说明可划分，即可结束
                    return True
        return False