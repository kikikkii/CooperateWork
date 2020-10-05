import collections
import itertools

class Board(object):
    def __init__(self,blocks,zero_column,zero_row):
        super().__init__()
        self.board = []
        self.zero_column = 0
        self.zero_row =0

        t = 0
        for i in blocks:
            self.board.append([])
            for j in i:
                self.board[t].append(j.number)
        self.zero_column = zero_column
        self.zero_row = zero_row
        self.zero_num = self.board[self.zero_row][self.zero_column]

    def slidingPuzzle(self):
        R, C = len(self.board), len(self.board[0])
        #self.board[self.zero_row][self.zero_column] = 0
        print(self.board)
        start = tuple(itertools.chain(*self.board))
        queue = collections.deque([(start, start.index(self.zero_num), 0)])
        seen = {start}
        operations = ""
        queueop = collections.deque()
        queueop.append(operations)
        print("--------------------------")
        target = tuple([range(1, R*C+1)])
        print(target)
        print("---------------------------")
        while queue:
            operations = queueop.popleft()
            #print(operations)
            board, posn, depth = queue.popleft()
            print("posn=" + str(posn))
            print("depth=" + str(depth))
            if board == target: return operations
            for d in (-1, 1, -C, C):
                if d == -1:
                    operations += "a"
                elif d == 1:
                    operations += "d"
                elif d == -C:
                    operations += "s"
                elif d == C:
                    operations += "w"
                nei = posn + d
                num = abs(nei//C - posn//C) + abs(nei%C - posn%C)
                print(num)
                if abs(nei//C - posn//C) + abs(nei%C - posn%C) != 1:
                   continue
                print("nei=" + str(nei))
                if 0 <= nei < R*C:
                    newboard = list(board)
                    print(newboard)
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    newt = tuple(newboard)
                    if newt not in seen:
                        print("add")
                        seen.add(newt)
                        queue.append((newt, nei, depth+1))
                        queueop.append(operations)

        return ""