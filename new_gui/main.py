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

import simulator
import getui
import dialog
import dataParsing
import stopwatch

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    Dialog = QtGui.QDialog()
    dia = dialog.Ui_Dialog()
    dia.setupUi(Dialog)
    Dialog.show()


    ui = simulator.Ui_MainWindow(dia)
    #get = getui.Getui()
    #get.setui(ui)
    ui.setupUi(MainWindow, ui)
    MainWindow.show()





    sys.exit(app.exec_())
