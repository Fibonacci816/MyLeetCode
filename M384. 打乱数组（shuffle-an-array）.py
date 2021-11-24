class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.nums = nums.copy()
        self.n = len(nums)

    # 时间O(1)
    def reset(self) -> List[int]:
        return self.ori

    # Fisher-Yates 洗牌算法（每次随机从牌堆中取出一张牌，直到取完）
    # 时间O(n)
    def shuffle(self) -> List[int]:
        for i in reversed(range(1, self.n)):
            j = int(random.random() * (i+1))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # 相当于每次把随机取出的牌放到最后
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()