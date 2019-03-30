# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 892)

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

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 30, 1251, 841))
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget.headerItem().setFont(1, font)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsDropEnabled
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setCheckState(0, QtCore.Qt.Checked)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setCheckState(0, QtCore.Qt.Checked)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsDragEnabled
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3.setFlags(
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEditable
            | QtCore.Qt.ItemIsDragEnabled
            | QtCore.Qt.ItemIsUserCheckable
            | QtCore.Qt.ItemIsEnabled
        )

        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(200)

        self.puchButton_add_donor = QtWidgets.QPushButton(self.centralwidget)
        self.puchButton_add_donor.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.puchButton_add_donor.setObjectName("puchButton_add_donor")
        
        self.pushButton_create_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_import.setEnabled(False)
        self.pushButton_create_import.setGeometry(QtCore.QRect(1120, 0, 120, 31))
        self.pushButton_create_import.setObjectName("pushButton_create_import")

        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(200, -7, 821, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        self.menuSubmenu1 = QtWidgets.QMenu(self.menuMenu)
        self.menuSubmenu1.setObjectName("menuSubmenu1")

        self.menuMenu2 = QtWidgets.QMenu(self.menubar)
        self.menuMenu2.setObjectName("menuMenu2")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionSubmenu = QtWidgets.QAction(MainWindow)
        self.actionSubmenu.setObjectName("actionSubmenu")

        self.actionSubmenu3 = QtWidgets.QAction(MainWindow)
        self.actionSubmenu3.setObjectName("actionSubmenu3")

        self.actionSubsubmenu1 = QtWidgets.QAction(MainWindow)
        self.actionSubsubmenu1.setObjectName("actionSubsubmenu1")

        self.actionSubsubmenu2 = QtWidgets.QAction(MainWindow)
        self.actionSubsubmenu2.setObjectName("actionSubsubmenu2")

        self.actionSubmenu_2 = QtWidgets.QAction(MainWindow)
        self.actionSubmenu_2.setObjectName("actionSubmenu_2")

        self.menuSubmenu1.addSeparator()
        self.menuSubmenu1.addAction(self.actionSubsubmenu1)
        self.menuSubmenu1.addAction(self.actionSubsubmenu2)

        self.menuMenu.addAction(self.menuSubmenu1.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSubmenu)
        self.menuMenu.addAction(self.actionSubmenu3)
        self.menuMenu2.addAction(self.actionSubmenu_2)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenu2.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "2", "test"))

        __sortingEnabled = self.treeWidget.isSortingEnabled()

        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Donor"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "AT001"))

        self.treeWidget.topLevelItem(0).child(0).setText(
            0, _translate("MainWindow", "Event")
        )
        self.treeWidget.topLevelItem(0).child(0).setText(
            1, _translate("MainWindow", "001")
        )

        self.treeWidget.topLevelItem(0).child(0).child(0).setText(
            0, _translate("MainWindow", "Serum")
        )

        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(
            0, _translate("MainWindow", "AT001-001-001")
        )
        self.treeWidget.topLevelItem(0).child(0).child(0).child(1).setText(
            0, _translate("MainWindow", "AT001-001-002")
        )

        self.treeWidget.topLevelItem(0).child(0).child(1).setText(
            0, _translate("MainWindow", "Plasma")
        )

        self.treeWidget.topLevelItem(0).child(0).child(1).child(0).setText(
            0, _translate("MainWindow", "AT001-001-003")
        )

        self.treeWidget.topLevelItem(0).child(0).child(2).setText(
            0, _translate("MainWindow", "WB(NAP) - Trizol")
        )

        self.treeWidget.topLevelItem(0).child(0).child(2).child(0).setText(
            0, _translate("MainWindow", "AT001-001-004")
        )

        self.treeWidget.topLevelItem(0).child(0).child(3).setText(
            0, _translate("MainWindow", "WB(NAP) - RNAlater")
        )

        self.treeWidget.topLevelItem(0).child(0).child(3).child(0).setText(
            0, _translate("MainWindow", "AT001-001-005")
        )

        self.treeWidget.topLevelItem(0).child(0).child(4).setText(
            0, _translate("MainWindow", "WB(NAP) - LB")
        )

        self.treeWidget.topLevelItem(0).child(0).child(4).child(0).setText(
            0, _translate("MainWindow", "AT001-001-006")
        )

        self.treeWidget.topLevelItem(0).child(0).child(5).setText(
            0, _translate("MainWindow", "Blood Card")
        )

        self.treeWidget.topLevelItem(0).child(0).child(5).child(0).setText(
            0, _translate("MainWindow", "AT001-001-007")
        )

        self.treeWidget.topLevelItem(0).child(0).child(6).setText(
            0, _translate("MainWindow", "Buffy(PBMC)")
        )

        self.treeWidget.topLevelItem(0).child(0).child(6).child(0).setText(
            0, _translate("MainWindow", "AT001-001-008")
        )

        self.treeWidget.topLevelItem(0).child(0).child(7).setText(
            0, _translate("MainWindow", "Buffy(PBMC) - RNAlater")
        )

        self.treeWidget.topLevelItem(0).child(0).child(7).child(0).setText(
            0, _translate("MainWindow", "AT001-001-009")
        )

        self.treeWidget.topLevelItem(1).setText(
            0, _translate("MainWindow", "Donor: AT002")
        )

        self.treeWidget.topLevelItem(1).child(0).setText(
            0, _translate("MainWindow", "Event: 001")
        )

        self.treeWidget.topLevelItem(1).child(0).child(0).setText(
            0, _translate("MainWindow", "Serum")
        )

        self.treeWidget.topLevelItem(1).child(0).child(0).child(0).setText(
            0, _translate("MainWindow", "AT002-001-001")
        )

        self.treeWidget.topLevelItem(1).child(1).setText(
            0, _translate("MainWindow", "Event: 002")
        )

        self.treeWidget.topLevelItem(1).child(1).child(0).setText(
            0, _translate("MainWindow", "Serum")
        )

        self.treeWidget.topLevelItem(1).child(1).child(0).child(0).setText(
            0, _translate("MainWindow", "AT002-002-001")
        )

        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.puchButton_add_donor.setText(_translate("MainWindow", "Add New Donor"))
        self.pushButton_create_import.setText(
            _translate("MainWindow", "Create Import Package")
        )
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:600; color:#ffffff;">Collection</span></p></body></html>',
            )
        )

        self.menuMenu.setTitle(_translate("MainWindow", "Menu1"))
        self.menuSubmenu1.setTitle(_translate("MainWindow", "Submenu1"))
        self.menuMenu2.setTitle(_translate("MainWindow", "Menu2"))

        self.actionSubmenu.setText(_translate("MainWindow", "Submenu2"))
        self.actionSubmenu3.setText(_translate("MainWindow", "Submenu3"))
        self.actionSubsubmenu1.setText(_translate("MainWindow", "Subsubmenu1"))
        self.actionSubsubmenu2.setText(_translate("MainWindow", "Subsubmenu2"))
        self.actionSubmenu_2.setText(_translate("MainWindow", "Submenu"))


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
