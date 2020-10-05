from PyQt5 import QtCore,QtGui,QtWidgets

class Tips(QtWidgets.QLabel):
    """description of class"""
    def __init__(self,Dialog):
        super().__init__(Dialog)
        self.setText("Tips")
        self.setGeometry(QtCore.QRect(610, 90, 130, 130))
        self.setScaledContents(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setObjectName("Tips")


