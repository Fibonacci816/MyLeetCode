class Solution:
    # 合并矩阵行为一个有序数组然后二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def merge(list1, list2):
            n1, n2 = len(list1), len(list2)
            res = []
            i, j = 0, 0
            while i < n1 and j < n2:
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i += 1
                else:
                    res.append(list2[j])
                    j += 1
            if i < n1:
                res.extend(list1[i:])
            if j < n2:
                res.extend(list2[j:])
            return res

        def bi_search(list, target):
            left, right = 0, len(list) - 1
            while left <= right:
                mid = (left + right) >> 1
                if list[mid] == target:
                    return True
                if list[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        while True:
            merge_list = []
            m = len(matrix)
            for i in range(0, m, 2):
                if i == m - 1:
                    merge_list.append(matrix[i]) 
                else:
                    merge_list.append(merge(matrix[i], matrix[i+1])) 
            if len(merge_list) == 1:
                break
            matrix = merge_list
        merge_list = merge_list[0]
        return bi_search(merge_list, target)

    # 从左下角开始折线查找
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False