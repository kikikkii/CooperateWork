from queue import Queue
from enum import IntEnum

class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
class sliddingPuzzle(object):
    def setBoard(self,blocks,zero_column,zero_row):
        self.board = Board(blocks,zero_column,zero_row)
        self.queue = Queue()

        self.seen = {}

    def slove(self):
        self.queue.put(self.board,self.operations)
        self.operations.copy()
        self.seen.update(self.board)
        while self.queue :
            board = self.queue.get()
            for direction in Direction:
                tempBoard = self.board.move(direction,self.board)
                if tempBoard not in seen:
                    self.queue.put(tempBoard)
                    self.seen.update(tempBoard)
    

    def check(self,board):
        t = 1
        for i in board:
            for j in i:
                if(j == t):
                    continue
                else:
                    return 0
        return 1

class Board(object):
    def __init__(blocks,zero_column,zero_row):
        board = []
        for i in blocks:
            board.append([])
            for j in i:
                board.append(j.number)
        self.zero_column = zero_column
        self.zero_row = zero_row
        self.operations = ""

    def move(self, direction,board):
        if(direction == Direction.UP): # 上
            if self.zero_row != 2:
                temp = board[self.zero_row][self.zero_column]
                board[self.zero_row][self.zero_column] = board[self.zero_row + 1][self.zero_column]
                board[self.zeor_row + 1][self.zero_column] = temp
                self.zero_row += 1
        if(direction == Direction.DOWN): # 下
            if self.zero_row != 0:
                temp = board[self.zero_row][self.zero_column]
                board[self.zero_row][self.zero_column] = board[self.zero_row - 1][self.zero_column]
                board[self.zeor_row - 1][self.zero_column] = temp
                self.zero_row -= 1
        if(direction == Direction.LEFT): # 左
            if self.zero_column != 2:
                temp = board[self.zero_row][self.zero_column]
                board[self.zero_row][self.zero_column] = board[self.zero_row][self.zero_column + 1]
                board[self.zeor_row][self.zero_column + 1] = temp
                self.zero_column += 1
        if(direction == Direction.RIGHT): # 右
            if self.zero_column != 0:
                temp = board[self.zero_row][self.zero_column]
                board[self.zero_row][self.zero_column] = board[self.zero_row][self.zero_column - 1]
                board[self.zeor_row][self.zero_column - 1] = temp
                self.zero_column -= 1
        return self