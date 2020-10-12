import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QFont, QPalette,QPixmap
from PyQt5.QtCore import Qt
import Button as bt
import HelpButton
import gridLayoutWidget as glw
import Tips

# 用枚举类表示方向

#游戏主体
class HuaRong(QtWidgets.QWidget):

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("HuaRong")
        Dialog.resize(966,655)
        #初始化"start"按钮
        self.startButton = bt.Button(Dialog)
        self.startButton.clicked.connect(self.startClick)
        #初始化"help"按钮
        self.helpButton = HelpButton.HelpButton(Dialog)
        self.helpButton.clicked.connect(self.helpClick)

        self.tips = Tips.Tips(Dialog)
        self.operates = ""
        self.show()
        
        #self.updatePanel()

    def keyPressEvent(self, event):
        self.gridLayoutWidget.keyPressEvent(event)

    #监听开始按钮
    def startClick(self):
        dict = self.startButton.click()
        self.gridLayoutWidget = glw.gridLayoutWidget(self.Dialog,dict)

    #监听帮助按钮
    def helpClick(self):
        board = self.gridLayoutWidget
        answer = self.helpButton.click(board)
        #给answer加入换行符
        
        self.tips.setText(answer)
    """description of class"""
        

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
  #MainWindow = QtWidgets.QWidget()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
  huarong = HuaRong()            # ui是你创建的ui类的实例化对象
  huarong.setupUi(huarong)         # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
  #MainWindow.show()            # 执行QMainWindow的show()方法，显示这个QMainWindow
  sys.exit(app.exec_())  
