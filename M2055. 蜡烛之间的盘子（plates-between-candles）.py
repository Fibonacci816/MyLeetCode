class Solution:
    # 预处理：分别存储位置i（包括i）左边满足条件的盘子数量、左边第一个蜡烛的位置和右边第一个蜡烛的位置
    # 时间O(n+q) 空间O(n)
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        paltes = {}
        n_plates = 0

        candle_left_idx = [-1] * n
        for i in range(n):
            if s[i] == '|':
                candle_left_idx[i] = i
                paltes[i] = n_plates
            elif i > 0:
                candle_left_idx[i] = candle_left_idx[i-1]
                n_plates += 1

        candle_right_idx = [-1] * n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                candle_right_idx[i] = i
            elif i < n - 1:
                candle_right_idx[i] = candle_right_idx[i+1]

        ans = []
        for left, right in queries:
            if candle_left_idx[right] == -1 or candle_right_idx[left] == -1 or candle_left_idx[right] <= candle_right_idx[left]:
                ans.append(0)
            else:
                ans.append(paltes[candle_left_idx[right]] - paltes[candle_right_idx[left]])
        return ans
