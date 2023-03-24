import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from NotesUI import Ui_MainWindow 

class Notes(QtWidgets.QMainWindow):

    
    def __init__(self):
        super(Notes, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.ui.pushButton.clicked.connect(self.save1)
        self.ui.pushButton_2.clicked.connect(self.save2)
        self.ui.pushButton_3.clicked.connect(self.save3)



    def init_ui(self):
        self.setWindowTitle('NoTes!')
        self.ui.text1.setPlaceholderText('Note 1')
        self.ui.text2.setPlaceholderText('Note 2')
        self.ui.text3.setPlaceholderText('Note 3')

    def save1(self):
        self.text1 = self.ui.text1.toPlainText()
        self.ui.text1.setPlaceholderText(self.text1)

    def save2(self):
        self.text2 = self.ui.text2.toPlainText()
        self.ui.text2.setPlaceholderText(self.text2)
    def save3(self):
        self.text3 = self.ui.text3.toPlainText()
        self.ui.text3.setPlaceholderText(self.text3)

app = QtWidgets.QApplication([])
application = Notes()
application.show()
sys.exit(app.exec())