class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    # 水塘抽样
    # 时间O(n) 空间O(1)
    def pick(self, target: int) -> int:
        ans, cnt = -1, 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randrange(cnt) == 0:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)