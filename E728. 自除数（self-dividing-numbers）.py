class Solution:
    # 时间O((r-l)logr) 空间O(1)
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            for d in str(num):
                if d == '0' or num % int(d) != 0:
                    return False
            return True
        return [num for num in range(left, right+1) if is_self_dividing(num)]
