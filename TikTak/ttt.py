import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow 
clicks = 1

class TikTakToe(QtWidgets.QMainWindow):
    global clicks
    def ex(self, clicks):
        if clicks == 10:
            continue
        elif self.ui.X1.text() == ('X') and self.ui.X2.text() == ('X') and self.ui.X3.text() == ('X') or self.ui.X1.text() == ('O') and self.ui.X2.text() == ('O') and self.ui.X3.text() == ('O'):
            sys.exit()
        elif self.ui.Y1.text() == ('X') and self.ui.Y2.text() == ('X') and self.ui.Y3.text() == ('X') or self.ui.Y1.text() == ('O') and self.ui.Y2.text() == ('O') and self.ui.Y3.text() == ('O'):
            sys.exit()
        elif self.ui.Z1.text() == ('X') and self.ui.Z2.text() == ('X') and self.ui.Z3.text() == ('X') or self.ui.Z1.text() == ('O') and self.ui.Z2.text() == ('O') and self.ui.Z3.text() == ('O'):
            sys.exit()
        elif self.ui.X1.text() == ('X') and self.ui.Y1.text() == ('X') and self.ui.Z1.text() == ('X') or self.ui.X1.text() == ('O') and self.ui.Y1.text() == ('O') and self.ui.Z1.text() == ('O'):
            sys.exit()
        elif self.ui.X2.text() == ('X') and self.ui.Y2.text() == ('X') and self.ui.Z2.text() == ('X') or self.ui.X2.text() == ('O') and self.ui.Y2.text() == ('O') and self.ui.Z2.text() == ('O'):
            sys.exit()
        elif self.ui.X3.text() == ('X') and self.ui.Y3.text() == ('X') and self.ui.Z3.text() == ('X') or self.ui.X3.text() == ('O') and self.ui.Y3.text() == ('O') and self.ui.Z3.text() == ('O'):
            sys.exit()
        elif self.ui.X1.text() == ('X') and self.ui.Y2.text() == ('X') and self.ui.Z3.text() == ('X') or self.ui.X1.text() == ('O') and self.ui.Y2.text() == ('O') and self.ui.Z3.text() == ('O'):
            sys.exit()
        elif self.ui.X3.text() == ('X') and self.ui.Y2.text() == ('X') and self.ui.Z1.text() == ('X') or self.ui.X3.text() == ('O') and self.ui.Y2.text() == ('O') and self.ui.Z1.text() == ('O'):
            sys.exit()
    def __init__(self):
        super(TikTakToe, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.X1.clicked.connect(self.X1)
        self.ui.X2.clicked.connect(self.X2)
        self.ui.X3.clicked.connect(self.X3)
        self.ui.Y1.clicked.connect(self.Y1)
        self.ui.Y2.clicked.connect(self.Y2)
        self.ui.Y3.clicked.connect(self.Y3)
        self.ui.Z1.clicked.connect(self.Z1)
        self.ui.Z2.clicked.connect(self.Z2)
        self.ui.Z3.clicked.connect(self.Z3)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Крестики Нолики')
        self.setWindowIcon(QIcon('icon.png'))

    def X1(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.X1.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.X1.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.X1.setEnabled(False)
    def X2(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.X2.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.X2.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.X2.setEnabled(False)
    def X3(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.X3.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.X3.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.X3.setEnabled(False)
    def Y1(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Y1.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Y1.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Y1.setEnabled(False)
    def Y2(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Y2.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Y2.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Y2.setEnabled(False)
    def Y3(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Y3.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Y3.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Y3.setEnabled(False)
    def Z1(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Z1.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Z1.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Z1.setEnabled(False)
    def Z2(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Z2.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Z2.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Z2.setEnabled(False)
    def Z3(self):
        global clicks
        if clicks % 2 == 1:
            self.ui.Z3.setText('X')
            clicks += 1
            self.ex(clicks)
        else:
            self.ui.Z3.setText('O')
            clicks += 1
            self.ex(clicks)
        self.ui.Z3.setEnabled(False)

app = QtWidgets.QApplication([])
application = TikTakToe()
application.show()
sys.exit(app.exec())
