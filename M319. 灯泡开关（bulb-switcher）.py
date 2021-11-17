class Solution:
    # 对于第i个灯泡，它被切换的次数恰好就是i的约数个数
    # 如果i的约数个数为偶数，那么一对操作相互抵消，所以第i个灯泡状态不变(为暗)
    # 只有完全平方数的约数个数为奇数， 所以1~n中完全平方数的个数（int(sqrt(n))）即为所求
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))  # + 0.5 是防止浮点数运算出现精度问题
