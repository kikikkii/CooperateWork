import sys
sys.path.append("..")
from PyQt5 import QtCore,QtGui,QtWidgets
import SloveTest

class HelpButton(QtWidgets.QPushButton):
    #初始化按钮
    def __init__(self,Dialog):
        super().__init__(Dialog)
        self.setObjectName("HelpButton")
        self.setGeometry(QtCore.QRect(160 * 2, 430 , 111, 61))
        self.setText("Help")

    def click(self,board):
        print("HelpButton clicked")
        theSolution = str(SloveTest.Solution(board.blocks,board.zero_column,board.zero_row).slidingPuzzle())
        print(theSolution)
        return theSolution
