class MyCalendar:

    def __init__(self):
        self.calendars = []

    # 二分查找
    # 时间O(logn) 空间O(n)
    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.calendars, end, key=lambda x: x[0])
        if i > 0 and self.calendars[i-1][1] > start:
            return False
        # 合并日程，非必要
        if i < len(self.calendars) and self.calendars[i][0] == end:
            self.calendars[i] = [start, self.calendars[i][1]]
            return True
        elif i > 0 and self.calendars[i-1][1] == start:
            self.calendars[i-1] = [self.calendars[i-1][0], end]
            return True
        self.calendars.insert(i, [start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)