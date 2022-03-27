class Solution:
    # 动态规划求出第i天前警卫数目连续非递增的天数和第i天后警卫数目连续非递减的天数，然后遍历一遍找出合适的日子
    # 时间O(n) 空间O(n)
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        no_incr = [0] * n
        no_decr = [0] * n
        for i in range(1, n-1):
            if security[i] <= security[i-1]:
                no_incr[i] = no_incr[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                no_decr[n-i-1] = no_decr[n-i] + 1
        return [i for i in range(time, n-time) if no_incr[i] >= time and no_decr[i] >= time]