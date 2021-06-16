class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        i, j = 0, 0
        mid_nums = []
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                mid_nums.append(nums1[i])
                i += 1
            else:
                mid_nums.append(nums2[j])
                j += 1
            if len(mid_nums) == total // 2 + 1:
                break
        while len(mid_nums) < total // 2 + 1 and i < n1:
            mid_nums.append(nums1[i])
            i += 1
        while len(mid_nums) < total // 2 + 1 and j < n2:
            mid_nums.append(nums2[j])
            j += 1
        return mid_nums[-1] if total % 2 else (mid_nums[-2] + mid_nums[-1]) / 2