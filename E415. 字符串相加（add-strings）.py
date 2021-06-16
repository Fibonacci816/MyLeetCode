class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        carry = 0
        res = ''
        for i in range(max(n1, n2)):
            int1 = int(num1[n1-i-1]) if n1-i-1 >= 0 else 0
            int2 = int(num2[n2-i-1]) if n2-i-1 >= 0 else 0
            s = int1 + int2 + carry
            res = str(s % 10) + res
            carry = s // 10
        return '1' + res if carry else res
