class Solution:
	# 模拟两数相乘运算过程
	# 时间O(mn) 空间O(m)
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        def digit_mul(nums, digit):
            res = []
            bit_add = 0
            for num in nums[::-1]:
                mul_ = num * digit + bit_add
                res.append(mul_ % 10)
                bit_add = mul_ // 10
            if bit_add != 0:
                res.append(bit_add)
            return res[::-1]

        def nums_add(num1, num2):
            num1 = num1[::-1]
            num2 = num2[::-1]
            res = []
            bit_add = 0
            n1, n2 = len(num1), len(num2)
            n = max(n1, n2)
            for i in range(n):
                sum_ = (num1[i] if i < n1 else 0) + (num2[i] if i < n2 else 0) + bit_add
                res.append(sum_ % 10)
                bit_add = sum_ // 10
            if bit_add != 0:
                res.append(bit_add)
            return res[::-1]

        num1 = [int(ch) for ch in num1]
        num2 = [int(ch) for ch in num2]
        res = []
        for i in range(n := len(num2)):
            sub_res = digit_mul(num1, num2[n-1-i]) + [0] * i
            if i == 0:
                res = sub_res
            else:
                res = nums_add(res, sub_res)
        res = [str(digit) for digit in res]
        return ''.join(res)
