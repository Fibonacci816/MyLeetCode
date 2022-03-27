class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n, idx = len(nums), 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return 0 if n == 0 else idx
