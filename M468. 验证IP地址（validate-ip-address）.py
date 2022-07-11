class Solution:
    # 遍历 + 判断
    # 时间O(n) 空间O(n)
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(q):
            split = q.split('.')
            if len(split) != 4:
                return False
            return all(map(lambda x: (len(x) == 1 or not x.startswith('0')) and x.isdigit() and 0 <= int(x) <= 255, split))

        def is_ipv6(q):
            split = q.split(':')
            if len(split) != 8:
                return False
            return all(map(lambda x: 1 <= len(x) <= 4  and all(map(lambda y: y.isdigit() or 'a' <= y.lower() <= 'f', x)), split))

        if is_ipv4(queryIP):
            return "IPv4"
        elif is_ipv6(queryIP):
            return "IPv6"
        return "Neither"