class Solution:
    # 双指针（两边向中间）
    # 时间O(n) 空间O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                return [left+1, right+1]
            if _sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]