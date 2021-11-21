# 深度优先搜索+剪枝
class Solution:
    def __init__(self):
        self.min_ball = -1
    def remove(self, board, i):
        all_board = []
        while True:
            if not board:
                break
            n = len(board)
            h = board[i]
            l = i - 1
            r = i + 1
            while l >= 0 and board[l] == h:
                l -= 1
            while r < n and board[r] == h:
                r += 1
            if r - l - 1 >= 3:
                board = board[:l+1] + board[r:]
                if l < 0 or r > n:
                    break
                i = l
            else:
                break
        return board
    
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))
        @lru_cache(None)
        def solve(board, hand, used):
            bn = len(board)
            hn = len(hand)
            if bn == 0 or hn == 0:
                if bn == 0 and (self.min_ball == -1 or self.min_ball > used):
                    self.min_ball = used
                return
            for i in range(bn+1):
                for j in range(hn):
                    if j > 0 and hand[j] == hand[j-1]:
                        continue
                    if i > 0 and board[i-1] == hand[j]:
                        continue
                    if not (i < len(board) and board[i] == hand[j]) and not (0 < i < len(board) and board[i-1] == board[i] and board[i-1] != hand[j]):
                        continue
                    new_board = self.remove(board[:i] + hand[j] + board[i:], i)
                    solve(new_board, hand[:j] + hand[j+1:], used + 1)
        solve(board, hand, 0)
        return self.min_ball

# 广度优先搜索+剪枝        
class Solution:
    def remove(self, board):
        n = 1
        while n:
            board, n = re.subn(r"(.)\1{2,}", "", board)
        return board

    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(hand))

        # 初始化用队列维护的状态队列：其中的三个元素分别为桌面球状态、手中球状态和回合数
        queue = deque([(board, hand, 0)])

        # 初始化用哈希集合维护的已访问过的状态
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # 第 1 个剪枝条件: 当前球的颜色和上一个球的颜色相同
                if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                    continue

                # 第 2 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球
                if i > 0 and cur_board[i - 1] == cur_hand[j]:
                    continue
                
                # 第 3 个剪枝条件: 只在以下两种情况放置新球
                choose = False
                #  - 第 1 种情况 : 当前球颜色与后面的球的颜色相同
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    choose = True
                #  - 第 2 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                    choose = True

                if choose:
                    new_board = self.remove(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    if not new_board:
                        return step + 1
                    if (new_board, new_hand) not in visited:
                        queue.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))
        return -1
        