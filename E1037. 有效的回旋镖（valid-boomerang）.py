class Solution:
    # 判断斜率是否相同
    # 时间O(1) 空间O(1)
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        if points[0][0] == points[1][0] == points[2][0]:
            return False
        return (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) != (points[2][1] - points[0][1]) / (points[2][0] - points[0][0]) if points[1][0] != points[0][0] and points[2][0] != points[0][0] else True

    # 叉乘（面积）不为0
    # 时间O(1) 空间O(1)
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = points[1][0] - points[0][0], points[1][1] - points[0][1]
        b = points[2][0] - points[0][0], points[2][1] - points[0][1]
        cross = a[0] * b[1] - a[1] * b[0]
        return cross != 0        