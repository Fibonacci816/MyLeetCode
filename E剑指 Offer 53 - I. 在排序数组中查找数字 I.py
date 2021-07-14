class Solution:
    # 一次二分+窗口扩展
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                add_l = 1
                while mid - add_l >= 0 and nums[mid - add_l] == target:
                    add_l += 1
                add_r = 1
                while mid + add_r < n and nums[mid + add_r] == target:
                    add_r += 1
                return (add_l - 1) + (add_r - 1) + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    # 两次二分
    def search(self, nums: List[int], target: int) -> int:
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        return find_right(nums, target) - find_left(nums, target) - 1