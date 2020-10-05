from PyQt5 import QtCore,QtGui,QtWidgets

class gridLayout(QtWidgets.QGridLayout):
    def __init__(self,LayoutWidget):
        super().__init__(LayoutWidget)
        self.setObjectName("gridLayout")
        self.setContentsMargins(0,0,0,0)
        

