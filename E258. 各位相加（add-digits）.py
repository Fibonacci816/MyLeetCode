class Solution:
    # 模拟
    def addDigits(self, num: int) -> int:
        def sum_digits(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total
        while num >= 10:
            num = sum_digits(num)
        return num

    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num > 0 else 0