class Solution:
    # 递增穷举
    # 时间O(n) 空间O(1)
    def isPerfectSquare(self, num: int) -> bool:
        x = square = 1
        while square <= num:
            if square == num:
                return True
            x += 1
            square = x * x
        return False

    # 二分查找
    # 时间O(logn) 空间O(1)
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False