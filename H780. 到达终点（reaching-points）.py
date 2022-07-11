class Solution:
    # 反向计算
    # 时间O(log(max(tx, ty))) 空间O(1)
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        if tx == sx and ty > sy and (ty - sy) % tx == 0:
            return True
        if ty == sy and tx > sx and (tx - sx) % ty == 0:
            return True
        return False