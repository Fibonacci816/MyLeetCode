class Solution:
    # 当满足完美矩形时，完美矩形总面积等于各个矩形面积之和且完美矩形四个顶点只出现一次，其余内部和边界点出现两次或四次
    # 时间O(n) 空间O(n)
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        total_area, lb_x, lb_y, rt_x, rt_y = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        point_cnt = defaultdict(int)
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            lb_x = min(lb_x, x1)
            lb_y = min(lb_y, y1)
            rt_x = max(rt_x, x2)
            rt_y = max(rt_y, y2)
            point_cnt[(x1, y1)] += 1
            point_cnt[(x1, y2)] += 1
            point_cnt[(x2, y2)] += 1
            point_cnt[(x2, y1)] += 1
        if (rt_x - lb_x) * (rt_y - lb_y) != total_area or point_cnt[(lb_x, lb_y)] != 1 or point_cnt[(lb_x, rt_y)] != 1 or point_cnt[(rt_x, rt_y)] != 1 or point_cnt[(rt_x, lb_y)] != 1:
            return False
        del point_cnt[(lb_x, lb_y)], point_cnt[(lb_x, rt_y)], point_cnt[(rt_x, rt_y)], point_cnt[(rt_x, lb_y)]
        return all(v == 2 or v == 4 for v in point_cnt.values())
        