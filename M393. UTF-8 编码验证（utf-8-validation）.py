class Solution:
    # 位运算
    # 时间O(n) 空间O(1)
    def validUtf8(self, data: List[int]) -> bool:
        mask1, mask2 = 1 << 7, (1 << 7) | (1 << 6)
        cnt = 0
        for d in data:
            if cnt == 0:
                mask = mask1
                i = 0
                while d & mask:
                    i += 1
                    mask >>= 1
                if i == 1 or i > 4:
                    return False
                cnt = i - 1 if i > 1 else 0
            else:
                if d & mask2 != mask1:
                    return False
                cnt -= 1
        return cnt == 0
