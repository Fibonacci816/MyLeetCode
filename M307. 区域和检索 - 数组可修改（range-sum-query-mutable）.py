# 分块
class NumArray:
    # 时间O(n) 空间O(√n)
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.n = len(nums) 
        self.size = int(self.n ** 0.5)
        self._sum = [0] * ((self.n + self.size - 1) // self.size)
        for i, num in enumerate(nums):
            self._sum[i//self.size] += num

    # 时间O(1)
    def update(self, index: int, val: int) -> None:
        self._sum[index//self.size] += val - self.arr[index]
        self.arr[index] = val

    # 时间O(√n)
    def sumRange(self, left: int, right: int) -> int:
        a, b = left // self.size, right // self.size
        if a == b:
            return sum(self.arr[left:right+1])
        else:
            return sum(self.arr[left:(a+1)*self.size]) + sum(self._sum[a+1:b]) + sum(self.arr[b*self.size:right+1])


class NumArray:
    # 时间O(nlogn) 空间O(n)
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.add(i+1, num)
    
    def lowbit(self, index):
        return index & (-index)
    
    def add(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)

    # 时间O(logn)
    def update(self, index: int, val: int) -> None:
        self.add(index+1, val-self.nums[index])
        self.nums[index] = val

    def pre_sum(self, index):
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= self.lowbit(index)
        return ans

    # 时间O(logn)
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum(right+1) - self.pre_sum(left)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)