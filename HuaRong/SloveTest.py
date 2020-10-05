import collections
import itertools
import heapq

class Solution(object):
    def __init__(self,blocks,zero_column,zero_row):
        super().__init__()
        self.board = []
        self.zero_column = 0
        self.zero_row =0

        self.zero_column = zero_column
        self.zero_row = zero_row
        t = 0
        for i in blocks:
            self.board.append([])
            for j in i:
                tmp = j.number
                self.board[t].append(tmp)
            t += 1
        self.zero_num = self.board[zero_row][zero_column]
        
    def slidingPuzzle(self):
        board = self.board
        R, C = len(board), len(board[0])
        #board[self.zero_row][self.zero_column] = 0
        start = tuple(itertools.chain(*board))
        #target = tuple([*range(1, R * C)] + [0])
        target = tuple([*range(1, R * C + 1)])
        #target_wrong = tuple([*range(1, R*C-2)] + [R*C-1, R*C-2, 0])
        operations = ""
        pq = [(0, 0, start, start.index(self.zero_num),operations)]
        cost = {start: 0}
        

        expected = {(C*r+c+1) % (R*C+1) : (r, c)
                    for r in range(R) for c in range(C)}
        def heuristic(board):
            ans = 0
            for r in range(R):
                for c in range(C):
                    val = board[C*r + c]
                    #if val == self.zero_num: continue
                    er, ec = expected[val]
                    ans += abs(r - er) + abs(c - ec)
            return ans

        while pq:
            #f = estimated distance (priority)
            #g = actual distance travelled (depth)
            f, g, board, zero, ops = heapq.heappop(pq)
            if board == target: return ops
            #if board == target_wrong: return -1
            if f > cost[board]: continue

            for delta in (-1, 1, -C, C):
                tops = ops
                if delta == -1:
                    tops += "d"
                elif delta == 1:
                    tops += "a"
                elif delta == -C:
                    tops += "s"
                elif delta == C:
                    tops += "w"
                nei = zero + delta
                if abs(zero // C - nei // C) + abs(zero % C - nei % C) != 1:
                    continue
                if 0 <= nei < R*C:
                    board2 = list(board)
                    board2[zero], board2[nei] = board2[nei], board2[zero]
                    board2t = tuple(board2)
                    ncost = g + 1 + heuristic(board2t)
                    if ncost < cost.get(board2t, float('inf')):
                        cost[board2t] = ncost
                        heapq.heappush(pq, (ncost, g+1, board2t, nei, tops))

        return -1
"""
boards = [[6,5,4],[7,8,3],[9,1,2]]
S = Solution()
depth = S.slidingPuzzle(boards)
print(depth)
print(len(depth))
"""