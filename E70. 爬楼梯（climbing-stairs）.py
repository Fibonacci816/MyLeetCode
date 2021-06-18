class Solution(object):
	# 动态规划迭代 f(n+1) = f(n-1) + f(n) 时间O(n) 空间O(1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1, f2 = 0, 1
        for i in range(n):
            f1, f2 = f2, f1 + f2
        return f2

    # 转化为矩阵递推F(n, n+1) = A · F(n-1, n) = A^n · F(0, 1) 时间O(logn) 空间O(1)
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        def matmul(A, B):
            res = [
                [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
            ]
            return res
        def qpow(A, n):
            res = [
                [1, 0],
                [0, 1]
            ]
            while n:
                if n & 1:
                    res = matmul(res, A)
                A = matmul(A, A)
                n >>= 1
            return res
        
        A = [
            [0, 1],
            [1, 1]
        ]
        B = qpow(A, n)
        return B[1][1]