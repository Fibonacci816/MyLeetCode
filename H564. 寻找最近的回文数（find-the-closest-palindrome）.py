class Solution:
    # 考虑所有的可能再进行比较
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        prefix = n[:(m + 1) // 2]
        suffix = n[:m // 2][::-1]
        if prefix + suffix != n:
            candidates.append(int(prefix + suffix))
        if m & 1:
            if prefix[-1] > '0':
                candidates.append(int(prefix[:-1] + chr(ord(prefix[-1])-1)+suffix))
            if prefix[-1] < '9':
                candidates.append(int(prefix[:-1] + chr(ord(prefix[-1])+1)+suffix))
        else:
            if prefix[-1] > '0':
                candidates.append(int(prefix[:-1] + chr(ord(prefix[-1])-1)*2+suffix[1:]))
            if prefix[-1] < '9':
                candidates.append(int(prefix[:-1] + chr(ord(prefix[-1])+1)*2+suffix[1:]))

        ans = candidates[0]
        selfNumber = int(n)
        for candidate in candidates[1:]:
            if abs(candidate - selfNumber) < abs(ans - selfNumber) or abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                ans = candidate
        return str(ans)
