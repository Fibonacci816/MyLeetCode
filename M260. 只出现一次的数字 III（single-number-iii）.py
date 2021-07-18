class Solution:
    # 分组异或
    # 时间O(n) 空间O(1)
    def singleNumber(self, nums: List[int]) -> List[int]:
        nor = 0
        for num in nums:
            nor ^= num
        idx = 1
        # 寻找异或结果第一位为1的位，待求的两个数的二进制在这一位必定不同，根据这一位进行分组即可将这两个数分到不同的组中
        while idx & nor == 0:
            idx <<= 1
        a, b = 0, 0
        # 两个组分别进行异或
        for num in nums:
            if idx & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
