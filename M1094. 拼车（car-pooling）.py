class Solution:
    # 差分数组
    # 时间O(n) 空间O(n)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for n, f, t in trips:
            diff[f] += n
            diff[t] -= n
        cur = 0
        for d in diff:
            cur += d
            if cur > capacity:
                return False
        return True
