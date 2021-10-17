# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # 古典概型 P1 * P2 = 1/10 (取P1 = 1/2, P2 = 1/5)
    def rand10(self):
        """
        :rtype: int
        """
        while (rnd1 := rand7()) == 7:
            continue
        while (rnd2 := rand7()) > 5:
            continue  
        return rnd2 if rnd1 < 4 else 5 + rnd2

    # (rand7-1) * 7 + rand7等概率生成[1, 49]，取[1, 40]
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            rnd1, rnd2 = rand7(), rand7()
            res = (rnd1 - 1) * 7 + rnd2
            if res <= 40:
                return 1 + (res - 1) % 10