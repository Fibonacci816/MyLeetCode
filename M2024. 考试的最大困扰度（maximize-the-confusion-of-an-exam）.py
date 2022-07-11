class Solution:
    # 滑动窗口
    # 时间O(n) 空间O(1)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChars(ch):
            ans, cnt, l = 0, 0, 0
            for r in range(len(answerKey)):
                cnt += answerKey[r] != ch
                while cnt > k:
                    cnt -= answerKey[l] != ch
                    l += 1
                ans = max(ans, r - l + 1)
            return ans
        return max(maxConsecutiveChars('T'), maxConsecutiveChars('F'))
