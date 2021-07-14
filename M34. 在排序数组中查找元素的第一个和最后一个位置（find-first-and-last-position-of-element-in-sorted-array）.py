class Solution:
    # 两次二分查找获取左右边界
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 获取左边界（即小于target且在target左边第一个数的位置，不存在返回-1）
        def get_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        # 获取右边界（即大于target且在target右边第一个数的位置，不存在返回数组长度）
        def get_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        left = get_left(nums, target) + 1
        right = get_right(nums, target) - 1  # 这里未指定查找范围，其实查找范围可以缩小为[left, len-1]
        return [left, right] if left <= right else [-1, -1]

    # 两次二分查找获取左右边界（右边界为小于(target+1)且在(target+1)左边第一个数的位置）
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def get_left(nums, left, right, target):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
            
        left = get_left(nums, 0, len(nums)-1, target) + 1
        right = get_left(nums, left, len(nums)-1, target+1)
        return [left, right] if left <= right else [-1, -1]
