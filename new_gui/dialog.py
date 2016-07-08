# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    pattern = '{0:02d} : {1:02d} : {2:02d}'

    timer = [0, 0, 0]
    state = True
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 361, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pause)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "00 : 00 : 00", None))


    def update_timeText(self):

        if(self.state):


            # Every time this function is called,
            # we will increment 1 centisecond (1/100 of a second)
            self.timer[2] += 1

            # Every 100 centisecond is equal to 1 second
            if (self.timer[2] >= 60):
                self.timer[2] = 0
                self.timer[1] += 1
            # Every 60 seconds is equal to 1 min
            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0
            # We create our time string here
            timeString = self.pattern.format(self.timer[0], self.timer[1], self.timer[2])
            # Update the timeText Label box with the current time
            #self.label.configure(text=timeString)
            self.label.setText(timeString)
            # Call the update_timeText() function after 1 centisecond



    # To start the kitchen timer
    def start(self):
        self.state = True

    # To pause the kitchen timer
    def pause(self):

        self.state = False

