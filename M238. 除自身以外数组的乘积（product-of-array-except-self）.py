class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, q = 1, 1
        res = [1]
        for num in nums[:-1]:
            p *= num
            res.append(p)
        for i in range(len(nums)-1, 0, -1):
            q *= nums[i]
            res[i-1] *= q
        return res