class Solution:
    # 暴力遍历
    # 时间O(n^2) 空间O(n)
    def bestRotation(self, nums: List[int]) -> int:
        def get_score(nums):
            score = 0
            for i, num in enumerate(nums):
                if num <= i:
                    score += 1
            return score

        n = len(nums)
        ans, max_score = 0, 0
        for i in range(n):
            tmp_nums = nums[i:] + nums[:i]
            score = get_score(tmp_nums)
            if max_score < score:
                ans, max_score = i, score
        return ans

    # 时间O(n) 空间O(n)
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0
        diffs = [0] * n
        for i, num in enumerate(nums):
            if num <= i:
                score += 1
            diffs[(i - num + n) % n] += 1
        # print(diffs)

        ans, max_score = 0, score
        for i in range(1, n):
            score -= diffs[i-1] - 1
            if score > max_score:
                ans, max_score = i, score
        return ans
