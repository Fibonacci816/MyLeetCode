class Solution:
	def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = [nums[0]]
        for num in nums[1:]:
            if d[-1] < num:
                d.append(num)
            else:
                left, right = 0, len(d) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if d[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                d[left] = num
        return len(d)

    # 粗暴动态规划
    def lengthOfLIS_Rough(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)            
        return max(dp)