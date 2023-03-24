# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.frame.setStyleSheet("background-color:#1A1E26")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.text1 = QtWidgets.QTextEdit(self.frame)
        self.text1.setGeometry(QtCore.QRect(0, 0, 400, 600))
        font = QtGui.QFont()
        font.setFamily("RomanD")
        font.setPointSize(18)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: #B9B4D9")
        self.text1.setObjectName("text1")
        self.b_refresh = QtWidgets.QPushButton(self.frame)
        self.b_refresh.setGeometry(QtCore.QRect(10, 540, 51, 51))
        self.b_refresh.setStyleSheet("QPushButton {\n"
"    background-color:#B9B4D9;\n"
"    border-radius: 12px;\n"
"    color: white;\n"
"    background-image: url();\n"
"    padding: 10px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #405173, stop:1 #283040);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #283040, stop:1 #405173);\n"
"    border-radius: 12px;\n"
"    color: white;\n"
"    background-image: url();\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.b_refresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("free-icon-font-refresh-3917766.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_refresh.setIcon(icon)
        self.b_refresh.setObjectName("b_refresh")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 0, 400, 600))
        self.frame_2.setStyleSheet("background-color: #283040")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.text2 = QtWidgets.QTextEdit(self.frame_2)
        self.text2.setGeometry(QtCore.QRect(0, 0, 400, 600))
        font = QtGui.QFont()
        font.setFamily("RomanD")
        font.setPointSize(18)
        self.text2.setFont(font)
        self.text2.setStyleSheet("color: #B9B4D9")
        self.text2.setObjectName("text2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(800, 0, 400, 600))
        self.frame_3.setStyleSheet("background-color: #405173;\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.text3 = QtWidgets.QTextEdit(self.frame_3)
        self.text3.setGeometry(QtCore.QRect(0, 0, 400, 600))
        font = QtGui.QFont()
        font.setFamily("RomanD")
        font.setPointSize(18)
        self.text3.setFont(font)
        self.text3.setStyleSheet("color: #B9B4D9")
        self.text3.setObjectName("text3")
        self.b_save = QtWidgets.QPushButton(self.frame_3)
        self.b_save.setGeometry(QtCore.QRect(340, 540, 51, 51))
        self.b_save.setStyleSheet("QPushButton {\n"
"    background-color:#B9B4D9;\n"
"    border-radius: 12px;\n"
"    color: white;\n"
"    background-image: url();\n"
"    padding: 10px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #405173, stop:1 #283040);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #283040, stop:1 #405173);\n"
"    border-radius: 12px;\n"
"    color: white;\n"
"    background-image: url();\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.b_save.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("free-icon-font-add-document-3914295.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_save.setIcon(icon1)
        self.b_save.setObjectName("b_save")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'RomanD\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'RomanD\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'RomanD\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'RomanD\';\"><br /></p></body></html>"))
