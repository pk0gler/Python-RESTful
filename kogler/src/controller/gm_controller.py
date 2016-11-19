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
    """ Creates the ClockController for the MVC - Application

       This class acts as the MainController for all interactions with
       the MainView.
       It connects the View with the Model

       - **Included Functions**
           Following Functions and methods can be invoked

           *init - Method*
           :func:`__init__`

           *reset - Method*
           :func:`reset`

           *submit - Method*
           :func:`submit`

           *getRadios - Method*
           :func:`getRadios`

           *keyPressEvent - Method*
           :func:`keyPressEvent`

       """

    def __init__(self):
        """ init Method

        Initiates the Controller
        Generates an Object of the view and the model

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
        """ reset - Method

        This method will be called when the user clicks the reset Button in the view
        It will reset all Values to its initial states

        """
        self.myView.lineEdit.setText("")
        self.myView.lineEdit_2.setText("")
        self.myView.label_4.setText("Geben Sie einen Start und ein Ziel ein")
        self.myView.textEdit.setText("")
        self.myView.radioButton.setChecked(True)
        self.myView.radioButton_3.setChecked(True)
        self.myView.radioButton_5.setChecked(True)

    def submit(self):
        """ submit - Method

        This Method will be called when the user clicks the Submit Button
        The input data will be passed to the model object which will create an HTTP Request
        After that the returned String will bes set for the output fields

        """
        self.getRadios()
        value = self.myModel.getData(self.myView.lineEdit.text(), self.myView.lineEdit_2.text(), self.mode, self.lang)
        self.myView.textEdit.setText(value.get('time') + value.get('instr'))
        self.myView.label_4.setText("Status: " + value.get('status'))

    def getRadios(self):
        """ getRadios - Method

        This Method is used to get the current State of all RadioButtons
        which will later be supplid to the HTTP - Request

        """
        for radio in self.myView.verticalGroupBox.findChildren(PS.QtGui.QRadioButton):
            if radio.isChecked() == True:
                self.mode = radio.text()

        for radio in self.myView.verticalGroupBox_3.findChildren(PS.QtGui.QRadioButton):
            if radio.isChecked() == True:
                self.lang = radio.text()

    def keyPressEvent(self, event):
        """ overrides keyPressEvent from QWidget

        This Method will be called when a Key in the focus range of the QWidget is called
        When the enter key is pressed and no input field is empty the submit method will be called

        :param event: key Event
        """
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
