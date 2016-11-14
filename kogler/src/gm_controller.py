from PySide.QtGui import *

from kogler.src.gm_model import Model
from kogler.src.gm_view import Ui_Form

import sys

class Controller(QWidget):

    def __init__(self):
        # Call Super Constructor (QMainWindow)
        super(Controller, self).__init__()
        # Initialize Attributes and class members
        self.myView = Ui_Form()
        self.myModel = Model()
        # Setup the view via setupUi (generated from pyuic)
        self.myView.setupUi(self)
        # Show View
        self.show()

    def reset(self):
        self.myView.lineEdit.setText("")
        self.myView.lineEdit_2.setText("")
        self.myView.label_4.setText("Geben Sie einen Start und ein Ziel ein")
        self.myView.textEdit.setText("")

    def submit(self):
        value = self.myModel.getData(self.myView.lineEdit.text(), self.myView.lineEdit_2.text())
        self.myView.textEdit.setText(value.get('time') + value.get('instr'))
        self.myView.label_4.setText("Status: " + value.get('status'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Controller()
    ret = app.exec_()
    sys.exit(ret)
