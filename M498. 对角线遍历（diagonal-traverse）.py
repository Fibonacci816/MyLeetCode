class Solution:
    # 元素行列位置下标的和确定它属于哪一条对角线
    # 依次遍历元素，加入到其对应的对角线数组中，再遍历每一个对角线数组，根据位置奇偶确定该数组正逆序
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diag_eles = [[] for i in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                diag_eles[i+j].append(mat[i][j])
        res = []
        for i, eles in enumerate(diag_eles):
            if i % 2 == 0:
                res.extend(eles[::-1])
            else:
                res.extend(eles)
        return res
