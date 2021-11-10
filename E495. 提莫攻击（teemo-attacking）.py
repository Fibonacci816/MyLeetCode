class Solution:
    # 一次扫描，根据两次攻击的时间差累计中毒时间
    # 时间O(n) 空间O(1)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(1, len(timeSeries)):
            time_diff = timeSeries[i] - timeSeries[i-1]
            total += duration if time_diff > duration else time_diff
        return total + duration

    # 一行代码（思路同上）
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return sum(duration if timeSeries[i] - timeSeries[i-1] > duration else timeSeries[i] - timeSeries[i-1] for i in range(1, len(timeSeries))) + duration
