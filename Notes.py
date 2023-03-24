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



    def init_ui(self):
        self.setWindowTitle('NoTes!')
        self.ui.text1.setPlaceholderText('Note 1')
        self.ui.text2.setPlaceholderText('Note 2')
        self.ui.text3.setPlaceholderText('Note 3')

    def save1(self):
        self.ui.text1.setPlaceholderText(self.note1)

        

app = QtWidgets.QApplication([])
application = Notes()
application.show()
sys.exit(app.exec())