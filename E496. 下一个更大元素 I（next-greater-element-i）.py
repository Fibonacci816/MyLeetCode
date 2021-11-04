class Solution:
    # 时间O(n2+n1) 空间O(n2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        low_seq = [nums2[0]]  # low_seq为单调递减序列
        idx_map = {nums2[0]: -1}
        for i in range(1, len(nums2)):
            idx_map[nums2[i]] = -1
            if nums2[i] > nums2[i-1]:
                while low_seq and low_seq[-1] < nums2[i]:
                    idx_map[low_seq.pop()] = nums2[i]
            low_seq.append(nums2[i])
        return [idx_map[num] for num in nums1]

    # 时间O(n2+n1) 空间O(n2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        low_stack = []  # low_seq为单调（递减）栈
        idx_map = {}
        for num in nums2[::-1]:
            while low_stack and low_stack[-1] < num:
                low_stack.pop()
            idx_map[num] = low_stack[-1] if low_stack else -1
            low_stack.append(num)
        return [idx_map[num] for num in nums1]
        