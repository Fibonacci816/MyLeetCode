class Solution:
    # 分情况讨论
    # 时间O(n) 空间O(1)
    def oneEditAway(self, first: str, second: str) -> bool:
        n1, n2 = len(first), len(second)
        if n1 < n2:
            first, second = second, first
            n1, n2 = n2, n1
        num_edit = 0
        if n1 == n2:
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    num_edit += 1
                if num_edit > 1:
                    return False
            return True
        elif n1 - n2 == 1:
            for i in range(n1):
                if i - num_edit == n2:
                    return True
                if first[i] != second[i-num_edit]:
                    num_edit += 1
                if num_edit > 1:
                    return False
            return True
        else:
            return False

    # 代码优化
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True
