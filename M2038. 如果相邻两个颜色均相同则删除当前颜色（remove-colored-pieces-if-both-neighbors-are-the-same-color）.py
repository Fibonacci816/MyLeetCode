class Solution:
    # 比较Alice 和 Bob的最大操作次数，因为Alice 和 Bob的操作相关独立，因此当Alice的操作数大于Bob的操作数时，Alice获胜
    # 时间O(n) 空间O(1)
    def winnerOfGame(self, colors: str) -> bool:
        score_a, score_b, cnt = 0, 0 ,0
        pre = 'C'
        for color in colors:
            if color == pre:
                cnt += 1
            else:
                cnt = 0
            if cnt > 1:
                if color == 'A':
                    score_a += 1
                else:
                    score_b += 1
            pre = color
        return score_a > score_b