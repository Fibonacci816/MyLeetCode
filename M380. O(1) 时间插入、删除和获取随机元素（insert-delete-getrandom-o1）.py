# 变长数组 + 哈希表
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        idx = self.set.pop(val)
        if idx != len(self.nums) - 1:
            self.nums[idx] = self.nums[-1]
            self.set[self.nums[-1]] = idx
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()