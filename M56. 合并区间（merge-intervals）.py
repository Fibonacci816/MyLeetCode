class Solution:
    # 时间O(nlogn) 空间O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        tmp = intervals[0]
        flag = True
        for i in range(1, len(intervals)):
            # 判断当前区间是否可以与前面的区间合并
            if tmp[1] >= intervals[i][0]:
                tmp = [tmp[0], max(tmp[1], intervals[i][1])]
            else:
                res.append(tmp)
                tmp = intervals[i]
        res.append(tmp)
        return res
