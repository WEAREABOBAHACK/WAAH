import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow 

class TikTakToe(QtWidgets.QMainWindow):
    def __init__(self):
        super(TikTakToe, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.X1.clicked.connect(self.game)
        self.ui.X2.clicked.connect(self.game)
        self.ui.X3.clicked.connect(self.game)
        self.ui.Y1.clicked.connect(self.game)
        self.ui.Y2.clicked.connect(self.game)
        self.ui.Y3.clicked.connect(self.game)
        self.ui.Z1.clicked.connect(self.game)
        self.ui.Z2.clicked.connect(self.game)
        self.ui.Z3.clicked.connect(self.game)
        self.init_ui()



    def init_ui(self):
        self.setWindowTitle('Крестики Нолики')
        self.setWindowIcon(QIcon('icon.png'))

    def game(self):
        self.ui.X1.setText('X')



app = QtWidgets.QApplication([])
application = TikTakToe()
application.show()
sys.exit(app.exec())


