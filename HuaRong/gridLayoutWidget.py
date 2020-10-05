import sys
sys.path.append("..")
import PicturesMatch.PicturesMatch as PM
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import gridLayout as gl
import Label
import SloveTest
from enum import IntEnum

class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class gridLayoutWidget(QtWidgets.QWidget):
    def __init__(self,Dialog,dict):
        super().__init__(Dialog)
        self.setObjectName("gridLayoutWidget")
        self.setGeometry(QtCore.QRect(160, 60, 341, 321))
        self.gridLayout = gl.gridLayout(self)
        #题目号初始化
        self.uuid = dict['uuid']
        self.step = dict['step']
        self.swap = dict['swap']
        self.blocks = []
        self.imgList = []
        self.zero_row = 0
        self.zero_column = 0
        self.operates = ""
        #获取图片,并将它放入九宫格
        for i in range(0,3):
            self.blocks.append([])
            for j in range(0,3):
                block = Label.Label(self,i * 3 + j)
                self.gridLayout.addWidget(block,i,j,1,1)
                self.blocks[i].append(block)
                #得到图片
                self.imgList.append(block.getImg())
                #if i * 3 + j == 0:#获取空白图片的位置
                    #self.zero_row = i
                    #self.zero_column = j
        #进行第一次比较,确定是哪张图片文件夹
        self.picturesLoad = PM.MatchFirst(self.imgList)
        #进行第二次比较,确定是哪张图
        Total = 45 #所有的图片序号之和
        for i in self.blocks:
            for j in i:
                j.number = PM.matchSecond(self.picturesLoad,j.getImg())
                Total -= j.number
                if j.number == 0 :
                    self.zero_column = j.column
                    self.zero_row = j.row
        print("j.column:" + str(self.zero_column))
        print("j.row:" + str(self.zero_row))
        self.blocks[self.zero_row][self.zero_column].number = Total
        print(Total)
        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        if(key == Qt.Key_Up or key == Qt.Key_W):
            self.move(Direction.UP)
        if(key == Qt.Key_Down or key == Qt.Key_S):
            self.move(Direction.DOWN)
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.move(Direction.LEFT)
        if(key == Qt.Key_Right or key == Qt.Key_D):
            self.move(Direction.RIGHT)
        self.updatePanel()
        print(self.zero_column,self.zero_row)
        #交换方块
        if(len(self.operates) == self.step):
            print("this is switch")
            print(self.swap)
            self.switch(self.swap[0],self.swap[1])
        #求解
        print("The solution is " + str(SloveTest.Solution(self.blocks,self.zero_column,self.zero_row).slidingPuzzle()))
        if self.checkResult():
            QMessageBox.Ok == QMessageBox.information(self, '挑战结果', '恭喜您完成挑战！')

    # 方块移动算法
    # 附加了输出每一步的操作内容
    def move(self, direction):
        if(direction == Direction.UP): # 上
            if self.zero_row != 2:
                temp = self.blocks[self.zero_row][self.zero_column]
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = temp
                self.zero_row += 1
                self.operates += "w"
                print(self.operates)
        if(direction == Direction.DOWN): # 下
            if self.zero_row != 0:
                temp = self.blocks[self.zero_row][self.zero_column]
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = temp
                self.zero_row -= 1
                self.operates += "s"
                print(self.operates)
        if(direction == Direction.LEFT): # 左
            if self.zero_column != 2:
                temp = self.blocks[self.zero_row][self.zero_column]
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = temp
                self.zero_column += 1
                self.operates += "a"
                print(self.operates)
        if(direction == Direction.RIGHT): # 右
            if self.zero_column != 0:
                temp = self.blocks[self.zero_row][self.zero_column]
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = temp
                self.zero_column -= 1
                self.operates += "d"
                print(self.operates)
    #更新棋盘，检查是否完成
    def updatePanel(self):
        for row in range(3):
            for column in range(3):
                self.gridLayout.addWidget((self.blocks[row][column]), row, column)

    #强制交换
    def switch(self,block1,block2):
        #判断是否有可移动方块
        block1_row = block1 // 3
        block1_column = block1 % 3
        block2_row = block2 // 3
        block2_column = block2 % 3
        if(block1_row == self.zero_row and block1_column == self.zero_column ):
            self.zero_row = block2_row
            self.zero_column = block2_column
        if(block2_row == self.zero_row and block2_column == self.zero_column ):
            self.zero_row = block1_row
            self.zero_column = block1_column

        temp = self.blocks[block1_row][block1_column]
        self.blocks[block1_row][block1_column] = self.blocks[block2_row][block2_column]
        self.blocks[block2_row][block2_column] = temp



    #检查是否完成
    def checkResult(self):
        check = 1
        for i in self.blocks:
            for j in i:
                if(j.number == check):
                    check += 1
                    continue
                return False
        return True
                
