class Solution:
    # 时间O(d) 空间O(d)，当1 <= n <= 2^31 - 1时d=9
    def findNthDigit(self, n: int) -> int:
        # 获取不大于i位的数的总数，i=1,2,...,d
        def total_digits(d):
            num = 9
            cur_sum = 0
            res = [0] * (d + 1)
            for i in range(1, d+1):
                cur_sum += i * num
                res[i] = cur_sum
                num *= 10
            return res
        _total_digits = total_digits(9)
        l, r = 1, 9
        # 二分查找确定n是几位数，循环退出时l的值即为n的位数，r = l - 1
        while l <= r:
            mid = (l + r) >> 1
            if _total_digits[mid] < n:
                l = mid + 1
            else:
                r = mid - 1
        idx = n - _total_digits[r] - 1  # idx为n在所有l位数构成的digit序列中的下标
        number = 10 ** r + idx // l  # number为第n个digit所属的数
        return int(str(number)[idx % l])  # idx % l 为第n个digit在number中的下标