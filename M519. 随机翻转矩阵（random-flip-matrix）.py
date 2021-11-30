class Solution:

    def __init__(self, m: int, n: int):
        self.n = n
        self.total = m * n
        self.choosen = set()

    def flip(self) -> List[int]:
        # 随机选下标，直到选中之前没有被选择过的下标
        while True:
            choice = random.randrange(self.total)
            if choice not in self.choosen:
                self.choosen.add(choice)
                break
        return [choice // self.n,  choice % self.n]

    def reset(self) -> None:
        self.choosen.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.left = self.m * self.n
        self.choosen = {}

    def flip(self) -> List[int]:
        choice = random.randrange(self.left)
        # 如果choice没有被选择，则self.choosen中没有choice
        # 否则choice位置为被交换的位置
        idx = self.choosen.get(choice, choice)
        self.left -= 1
        # 将self.left位置赋给choice
        self.choosen[choice] = self.choosen.get(self.left, self.left)
        return [idx // self.n,  idx % self.n]

    def reset(self) -> None:
        self.left = self.m * self.n
        self.choosen.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
