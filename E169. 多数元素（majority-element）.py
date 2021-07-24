class Solution:
    # Boyer-Moore 投票算法
    # 时间O(n) 空间O(1)
    def majorityElement(self, nums: List[int]) -> int:
        candidate, cnt = nums[0], 1
        for num in nums[1:]:
            if num == candidate:
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    candidate = num
                    cnt = 1
        return candidate