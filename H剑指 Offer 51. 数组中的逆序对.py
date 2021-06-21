class Solution:
    def __init__(self):
        self.reverse_num = 0
    # 归并排序过程中计算逆序对数量（子区间逆序对数量和+跨区间逆序对数量）
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums1, nums2):
            n1, n2 = len(nums1), len(nums2)
            nums = []
            i = 0
            for j in range(n2):
                while i < n1 and nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                nums.append(nums2[j])
                self.reverse_num += n1 - i
            nums += nums1[i:]
            return nums
                
        def merge_sort(nums):
            n = len(nums)
            if n < 2:
                return nums
            mid = n // 2
            nums1 = merge_sort(nums[:mid])
            nums2 = merge_sort(nums[mid:])
            if nums1[-1] <= nums2[0]:
                return nums1 + nums2
            return merge(nums1, nums2)
        
        merge_sort(nums)
        return self.reverse_num
