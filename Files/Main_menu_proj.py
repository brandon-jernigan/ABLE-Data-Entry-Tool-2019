# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Able Data Entry Tool")
        MainWindow.resize(600, 683)
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.snowflake = QtWidgets.QLabel(self.centralwidget)
        self.snowflake.setGeometry(QtCore.QRect(0, -20, 600, 600))
        self.snowflake.setText("")
        self.snowflake.setPixmap(QtGui.QPixmap("snowflake2_og.jpg"))
        self.snowflake.setScaledContents(True)
        self.snowflake.setAlignment(QtCore.Qt.AlignCenter)
        self.snowflake.setObjectName("snowflake")
        
        self.comboBox_option = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_option.setGeometry(QtCore.QRect(190, 560, 211, 22))
        self.comboBox_option.setAutoFillBackground(False)
        self.comboBox_option.setObjectName("comboBox_option")
        self.comboBox_option.addItem("")
        self.comboBox_option.addItem("")
        self.comboBox_option.addItem("")
        
        self.comboBox_collection = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_collection.setEnabled(True)
        self.comboBox_collection.setGeometry(QtCore.QRect(190, 590, 211, 22))
        self.comboBox_collection.setObjectName("comboBox_collection")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        
        self.statusbar.setPalette(palette)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
#        if self.comboBox_option.currentText() == 'Register Samples':
#            print('Register Samples')
        self.comboBox_option.currentTextChanged['QString'].connect(self.option_selection_changed)
        self.comboBox_collection.currentTextChanged['QString'].connect(self.collection_selection_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def option_selection_changed(self, selection):
        print("Option Selection Changed")
        print(str(selection))
        if str(selection) == "Reserve Kits" or str(selection) == "Register Samples":
            self.comboBox_collection.show()
        else:
            self.comboBox_collection.hide()
            self.comboBox_collection.setCurrentIndex(0)
        
    def collection_selection_changed(self, selection):
        print("Collection Selection Changed")
        print(str(selection))
        if str(selection) != "<Select Collection>":
            pass
            
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_option.setItemText(0, _translate("MainWindow", "<Select Option>"))
        self.comboBox_option.setItemText(1, _translate("MainWindow", "Reserve Kits"))
        self.comboBox_option.setItemText(2, _translate("MainWindow", "Register Samples"))
        self.comboBox_collection.setItemText(0, _translate("MainWindow", "<Select Collection>"))
        self.comboBox_collection.setItemText(1, _translate("MainWindow", "[AR] Trauma"))
        self.comboBox_collection.setItemText(2, _translate("MainWindow", "[AT] CDDOM (Mandarino/Diabetes)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

