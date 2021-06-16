class Solution:
    # 二分查找
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

    def mySqrt2(x):
        """
        :type x: int
        :rtype: int
        """
        # 限制精度
        def mySqrtByEpsilon(x, epsilon=1e-2):
            l, r = 0, x
            res = x
            while l <= r:
                mid = (l + r) / 2.0
                if mid * mid == x:
                    return mid
                if mid * mid < x:
                    res = mid
                    l = mid + epsilon / 2.0
                else:
                    r = mid - epsilon / 2.0
            return res

        res = int(mySqrtByEpsilon(x, 1))
        return res + 1 if (res + 1) ** 2 <= x else res