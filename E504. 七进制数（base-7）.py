class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans, prefix = "", ""
        if num < 0:
            num = -num
            prefix = '-'
        while num:
            ans = str(num % 7) + ans
            num //= 7
        return prefix + ans
