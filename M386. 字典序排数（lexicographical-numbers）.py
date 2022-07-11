class Solution:
    # 十叉树深度优先遍历（递归）
    # 时间O(n) 空间O(n)
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(start):
            if start > n: return
            ans.append(start)
            for i in range(10):
                dfs(start * 10 + i)
                
        for i in range(1, 10):
            dfs(i)
        return ans

    # 十叉树深度优先遍历（迭代）
    # 时间O(n) 空间O(1)
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans
