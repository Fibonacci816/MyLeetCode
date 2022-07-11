class Solution:
    # 二分查找
    # 时间O(nlogm)（m为 piles 中的最大值） 空间O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) >> 1
            if sum(map(lambda x: (x + mid - 1) // mid, piles)) > h:
                l = mid + 1
            else:
                r = mid
        return l
