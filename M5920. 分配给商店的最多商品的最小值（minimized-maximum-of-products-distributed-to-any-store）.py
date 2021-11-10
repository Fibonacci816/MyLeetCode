class Solution:
    # 二分查找
    # 时间O(len(quantities)log(max(quantities))) 空间O(1)
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)  # 商店商品数目最大值的上下界
        while l <= r:
            mid = (l + r) >> 1
            need = 0
            for quantitie in quantities:
                need += (quantitie - 1) // mid + 1
            if need <= n:
                r = mid - 1
            else:
                l = mid + 1
        return l
        