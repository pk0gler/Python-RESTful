"""
This Module represents the logical Controller of the Simple Game.
Its main purpose is the creation of View and Model as well as connecting
those components in one single Application
"""

import sys

import PySide as PS
from PySide.QtGui import *
from PySide.QtCore import *
from pysideuic.Compiler.qtproxies import QtCore

from kogler.src.model.gm_model import Model
from kogler.src.view.gm_view import Ui_Form


class Controller(QWidget):
    """ Creates the ClockController for the (M)VC - Application

       This class acts as the MainController for all interactions with
       the MainView.
       It connects the View with the Model

       - **Included Functions**
           Following Functions and methods can be invoked

           *init - Method*
           :func:`__init__`

           *game_start_game_loop - Method*
           :func:`start_game_loop`

           *initiate_buttons - Method*
           :func:`initiate_buttons`

           *change_mode - Method*
           :func:`change_mode`

       """

    def __init__(self):
        """ init Method

        bla

        """
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
        self.myView.radioButton.setChecked(True)
        self.myView.radioButton_3.setChecked(True)
        self.myView.radioButton_5.setChecked(True)

    def submit(self):
        self.getRadios()
        value = self.myModel.getData(self.myView.lineEdit.text(), self.myView.lineEdit_2.text(), self.mode, self.lang)
        self.myView.textEdit.setText(value.get('time') + value.get('instr'))
        self.myView.label_4.setText("Status: " + value.get('status'))

    def getRadios(self):
        for radio in self.myView.verticalGroupBox.findChildren(PS.QtGui.QRadioButton):
            if radio.isChecked() == True:
                self.mode = radio.text()

        for radio in self.myView.verticalGroupBox_3.findChildren(PS.QtGui.QRadioButton):
            if radio.isChecked() == True:
                self.lang = radio.text()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            if self.myView.lineEdit.text() == "" or self.myView.lineEdit_2.text() == "":
                self.myView.label_4.setText("Status: Bitte Geben Sie Start und Ziel ein")
            else:
                self.submit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Controller()
    ret = app.exec_()
    sys.exit(ret)
