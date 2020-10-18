import sys
sys.path.append("..")
from PyQt5 import QtCore,QtGui,QtWidgets
import RequestTest
import imageCutTest
from PIL import Image
from Competion import getListAPI,getQuestion

class Button(QtWidgets.QPushButton):
    #初始化按钮
    def __init__(self,Dialog):
        super().__init__(Dialog)
        self.setObjectName("GameStart")
        self.setGeometry(QtCore.QRect(160, 430, 111, 61))
        self.setText("start")
        #比赛专用计数
        self.num = 0

    def click(self):
        print("Button clicked")
        #dict = RequestTest.request()
        dict = getQuestion.getQuestion(self.num)
        self.num += 1
        Img = Image.open(".\imgtest.jpg")
        Img_list = imageCutTest.cut_image(Img)
        imageCutTest.save_images2(Img_list)
        return dict
    """description of class"""


