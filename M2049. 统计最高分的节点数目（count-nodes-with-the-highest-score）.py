class Solution:
    def __init__(self):
        self.max_score = 0
        self.count = 0

    # 后序遍历求子树大小和分数
    def get_size(self, root):
        size = 1
        score = 1
        for child in self.children[root]:
            sub_size = self.get_size(child)
            score *= sub_size
            size += sub_size
        if self.parents[root] != -1:
            score *= self.n - size
        # print(root, score)
        if score > self.max_score:
            self.max_score, self.count = score, 1
        elif score == self.max_score:
            self.count += 1
        return size

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.parents = parents
        self.n = len(parents)
        self.children = [[] for _ in range(self.n)]
        for i, parent in enumerate(parents):
            if parent != -1:
                self.children[parent].append(i)
        self.get_size(0)
        return self.count
