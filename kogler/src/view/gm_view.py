# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/philippkogler/Documents/PyCharm/Python-RESTful/kogler/ui/google_maps_restful.ui'
#
# Created: Mon Nov 14 21:29:16 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 569)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("padding: 10px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 3.5px;\n"
"border-color: #00695C;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"padding: 3.5px;\n"
"background-color: #80CBC4;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #FFFFFF;\n"
"    color:black\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setStyleSheet("QLabel {\n"
"padding: 7px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"margin: 5;\n"
"width: 50%;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #00695C;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"padding: 7px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"margin: 5;\n"
"width: 50%;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #00695C;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"padding: 3.5px;\n"
"background-color: #80CBC4;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #FFFFFF;\n"
"    color:black\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalGroupBox = QtGui.QGroupBox(Form)
        self.verticalGroupBox.setFlat(True)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.verticalGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtGui.QLabel(self.verticalGroupBox)
        self.label_7.setStyleSheet("QLabel {\n"
"padding: 5px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"border-width:10px;\n"
"border-color: #00695C;\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.verticalGroupBox)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.verticalGroupBox)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.verticalGroupBox)
        self.radioButton.setEnabled(True)
        self.radioButton.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 3, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.verticalGroupBox)
        self.verticalGroupBox_3 = QtGui.QGroupBox(Form)
        self.verticalGroupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalGroupBox_3.setFlat(True)
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtGui.QLabel(self.verticalGroupBox_3)
        self.label_5.setStyleSheet("QLabel {\n"
"padding: 5px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"border-width:10px;\n"
"border-color: #00695C;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.radioButton_5 = QtGui.QRadioButton(self.verticalGroupBox_3)
        self.radioButton_5.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.radioButton_4 = QtGui.QRadioButton(self.verticalGroupBox_3)
        self.radioButton_4.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_5.addWidget(self.radioButton_4)
        self.radioButton_6 = QtGui.QRadioButton(self.verticalGroupBox_3)
        self.radioButton_6.setStyleSheet("* {\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    background-color: #80CBC4;\n"
"    color: white;\n"
"}")
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_5.addWidget(self.radioButton_6)
        self.horizontalLayout_3.addWidget(self.verticalGroupBox_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setStyleSheet("QLabel {\n"
"padding: 7px;\n"
"background-color:#009688;\n"
"border-style: outset;\n"
"color:white;\n"
"border-width: 1px;\n"
"border-color: #00695C;\n"
"border-width: 2px;\n"
"border-color: #00695C;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setStyleSheet("margin: 5;\n"
"border: 5px solid #00695C;\n"
"background-color: #009688;\n"
"color: white;\n"
"padding:15px;\n"
"\n"
"div {\n"
"    margin-left: 5px;\n"
"}")
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 18px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 5px;\n"
"}\n"
"\n"
"QPushButton:hover,active{\n"
"    background-color:#388E3C;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #009688; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 18px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 5px;\n"
"}\n"
"\n"
"QPushButton:hover,focus {\n"
"    background-color: #00695C;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #F44336; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 16px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 5px;\n"
"}\n"
"\n"
"QPushButton:hover,focus {\n"
"    background-color: #D32F2F;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), Form.reset)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Form.submit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Google Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Ziel:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Transportation", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Form", "  Walking", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Form", "  Bicycling", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Form", "  Driving", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("Form", "  DE", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("Form", "  EN", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_6.setText(QtGui.QApplication.translate("Form", "  EL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Status: Geben Sie einen Start und ein Ziel ein", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
