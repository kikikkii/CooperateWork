import sys
sys.path.append("..")
import PicturesMatch
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QFont, QPalette,QPixmap

#Label控件，显示题目图片
class Label(QtWidgets.QLabel):
    #初始化函数
    def __init__(self,gridLayoutWidget,i):
        super().__init__(gridLayoutWidget)
        self.number = i + 1 #序号
        self.setFixedSize(90, 90)
        #self.setText(str(i))
        self.pixmap = QPixmap()#图片
        self.setObjectName("picture" + str(i))
        #self.pixmap.load("C:/Users/lbh/Desktop/SoftwareProject/CooperateWork/getPictures/" + (str)(self.number) + ".jpg")#这里先用绝对路径
        self.pixmap.load("./getPictures/" + (str)(self.number) + ".jpg")
        print(self.pixmap)
        #self.setStyleSheet("background-color:red;border-radius:10px;")
        self.setPixmap(self.pixmap)
        self.setScaledContents(True)
        self.row = int(i / 3)
        self.column = i % 3

    #获得Img
    def getImg(self):
        return self.pixmap
