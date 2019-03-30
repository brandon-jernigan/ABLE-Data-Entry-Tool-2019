# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.snowflake.setGeometry(QtCore.QRect(0, -10, 600, 600))
        self.snowflake.setText("")
        self.snowflake.setPixmap(QtGui.QPixmap("snowflake2_og.jpg"))
        self.snowflake.setScaledContents(True)
        self.snowflake.setAlignment(QtCore.Qt.AlignCenter)
        self.snowflake.setObjectName("snowflake")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 550, 601, 201))
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page_initial = QtWidgets.QWidget()
        self.page_initial.setObjectName("page_initial")
        
        self.lineEdit_init = QtWidgets.QLineEdit(self.page_initial)
        self.lineEdit_init.setGeometry(QtCore.QRect(260, 30, 71, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.lineEdit_init.setFont(font)
        self.lineEdit_init.setText("")
        self.lineEdit_init.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_init.setObjectName("lineEdit_init")
        
        self.label = QtWidgets.QLabel(self.page_initial)
        self.label.setGeometry(QtCore.QRect(200, 0, 191, 31))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.pushButton_go = QtWidgets.QPushButton(self.page_initial)
        self.pushButton_go.setEnabled(False)
        self.pushButton_go.setGeometry(QtCore.QRect(340, 30, 31, 31))
        self.pushButton_go.setObjectName("pushButton_go")
        
        self.stackedWidget.addWidget(self.page_initial)
        
        self.page_options = QtWidgets.QWidget()
        self.page_options.setObjectName("page_options")
        
        self.comboBox_option = QtWidgets.QComboBox(self.page_options)
        self.comboBox_option.setGeometry(QtCore.QRect(190, 10, 211, 22))
        self.comboBox_option.setAutoFillBackground(False)
        self.comboBox_option.setObjectName("comboBox_option")
        self.comboBox_option.addItem("")
        self.comboBox_option.addItem("")
        self.comboBox_option.addItem("")
        
        self.pushButton_go2 = QtWidgets.QPushButton(self.page_options)
        self.pushButton_go2.setGeometry(QtCore.QRect(410, 10, 31, 23))
        self.pushButton_go2.setObjectName("pushButton_go2")
        self.pushButton_go2.hide()
        
        self.pushButton_go3 = QtWidgets.QPushButton(self.page_options)
        self.pushButton_go3.setGeometry(QtCore.QRect(410, 40, 31, 23))
        self.pushButton_go3.setObjectName("pushButton_go3")
        self.pushButton_go3.hide()
        
        self.comboBox_collection = QtWidgets.QComboBox(self.page_options)
        self.comboBox_collection.setEnabled(True)
        self.comboBox_collection.setGeometry(QtCore.QRect(190, 40, 211, 22))
        self.comboBox_collection.setObjectName("comboBox_collection")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.addItem("")
        self.comboBox_collection.hide()
        
        self.stackedWidget.addWidget(self.page_options)
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
        
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionLogout)
        
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        
        self.comboBox_option.currentIndexChanged['QString'].connect(self.comboBox_collection.show)
        
        self.comboBox_option.currentTextChanged['QString'].connect(self.option_selection_changed)
        self.comboBox_collection.currentTextChanged['QString'].connect(self.collection_selection_changed)
        self.pushButton_go.clicked.connect(self.pushButton_go_clicked)
        self.lineEdit_init.textChanged.connect(self.lineEdit_init_edited)
        self.lineEdit_init.returnPressed.connect(self.pushButton_go_clicked)
        
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
            self.pushButton_go3.show()
        else:
            self.pushButton_go3.hide()

    def pushButton_go_clicked(self):
        print("Go button clicked")
        entered_text = str(self.lineEdit_init.text()).upper().strip()

        
        if entered_text:
            self.stackedWidget.setCurrentIndex(1)
        
        
    def lineEdit_init_edited(self):
        
        entered_text = str(self.lineEdit_init.text()).upper()
        
        self.lineEdit_init.setText(entered_text)
        
        entered_text = entered_text.strip()
        
        if entered_text:
            self.pushButton_go.setEnabled(True)
        else:
            self.pushButton_go.setEnabled(False)
                                   
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please enter your initials:"))
        self.pushButton_go.setText(_translate("MainWindow", "Go"))
        self.comboBox_option.setItemText(0, _translate("MainWindow", "<Select Option>"))
        self.comboBox_option.setItemText(1, _translate("MainWindow", "Reserve Kits"))
        self.comboBox_option.setItemText(2, _translate("MainWindow", "Register Samples"))
        self.pushButton_go2.setText(_translate("MainWindow", "Go"))
        self.pushButton_go3.setText(_translate("MainWindow", "Go"))
        self.comboBox_collection.setItemText(0, _translate("MainWindow", "<Select Collection>"))
        self.comboBox_collection.setItemText(1, _translate("MainWindow", "[AR] Trauma"))
        self.comboBox_collection.setItemText(2, _translate("MainWindow", "[AT] CDDOM (Mandarino/Diabetes)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLogout.setText(_translate("MainWindow", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.raise_()
    MainWindow.activateWindow()
    sys.exit(app.exec_())

