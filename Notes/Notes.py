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
        self.ui.b_save.clicked.connect(self.save)
        self.ui.b_refresh.clicked.connect(self.opensave)

    def init_ui(self):
        self.setWindowTitle('NoTes!')
        self.setWindowIcon(QIcon('Iconnote.png'))
        self.ui.text1.setPlaceholderText('Note 1')
        self.ui.text2.setPlaceholderText('Note 2')
        self.ui.text3.setPlaceholderText('Note 3')

    def save(self):
        self.text1 = self.ui.text1.toPlainText()
        self.ui.text1.setPlaceholderText(self.text1)
        file = open("Note1.txt", "w+")
        file.write(self.text1)
        file.close()
        self.text2 = self.ui.text2.toPlainText()
        self.ui.text2.setPlaceholderText(self.text2)
        file = open("Note2.txt", "w+")
        file.write(self.text2)
        file.close()
        self.text3 = self.ui.text3.toPlainText()
        self.ui.text3.setPlaceholderText(self.text3)
        file = open("Note3.txt", "w+")
        file.write(self.text3)
        file.close()

    def opensave(self):
        with open("Note1.txt", "r") as file:
            self.ui.text1.setText(file.read())
            file.close()

        with open("Note2.txt", "r") as file:
            self.ui.text2.setText(file.read())
            file.close()

        with open("Note3.txt", "r") as file:
            self.ui.text3.setText(file.read())
            file.close()



app = QtWidgets.QApplication([])
application = Notes()
application.show()
sys.exit(app.exec())