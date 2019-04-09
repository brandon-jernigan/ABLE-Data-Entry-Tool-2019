# -*- coding: utf-8 -*-
"""
@author: Taar
"""

# conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/6_treeview

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt as qt

ROWS = 2
COLS = 4


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        treeView = QtWidgets.QTreeView(self)
        self.setCentralWidget(treeView)
        standardModel = QtGui.QStandardItemModel()
        preparedRow = self.prepareRow("first", "second", "third", "fourth")
        item = standardModel.invisibleRootItem()
        item.appendRow(preparedRow)
        secondRow = self.prepareRow("111", "222", "333", "444")
        preparedRow[0].appendRow(secondRow)
        thirdRow = self.prepareRow("111", "222", "333", "444")
        preparedRow[0].appendRow(thirdRow)
        treeView.setModel(standardModel)
        treeView.expandAll()

    def prepareRow(self, first, second, third, fourth):
        rowItems = [
            QtGui.QStandardItem(first),
            QtGui.QStandardItem(second),
            QtGui.QStandardItem(third),
            QtGui.QStandardItem(fourth),
        ]
        return rowItems


if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(None)
    w.show()
    app.exec_()
