from PyQt5.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
    QPushButton,
    QLabel,
    QDialog,
    QVBoxLayout,
    QApplication,
    QLineEdit,
    QHBoxLayout,
)
from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class TreeWidgetWithWidgetItems(QDialog):
    def __init__(self):
        super(TreeWidgetWithWidgetItems, self).__init__()
        self.init_ui()

    def init_ui(self):
        # Creating the required widgets
        self.vboxLayout = QVBoxLayout()
        self.treeWidget = QTreeWidget()
        self.label = QLabel("I'm going to inform you about the buttons")
        # Adding the widgets
        self.vboxLayout.addWidget(self.treeWidget)
        self.vboxLayout.addWidget(self.label)
        self.treeWidget.setHeaderLabel("TreeWidget with Buttons")
        self.topLevelItem = QTreeWidgetItem()
        # Creating top level and child widgets
        self.topLevelButton = QPushButton("Top Level Button")
        self.multi = MultiWidget()
        self.childButton_1 = QPushButton("Child 1")
        self.childButton_2 = QPushButton("Child 2")
        self.childButton_2.setStyleSheet("border:1px solid rgb(255, 170, 255);")
        self.childButton_3 = QPushButton("Child 3")
        self.childLineEdit = QLineEdit()
        self.childLineEdit.setPlaceholderText("Add Text Here")
        # .................(contd) .... part-1

        # ..................(contd) ... from part-1
        # Adding the child to the top level item
        self.childItems = []
        self.treeWidget.setColumnCount(2)

        for i in range(4):
            self.childItems.append(QTreeWidgetItem())
            self.topLevelItem.addChild(self.childItems[i])
        self.treeWidget.addTopLevelItem(self.topLevelItem)
        # self.treeWidget.setItemWidget(self.topLevelItem, 1, self.topLevelButton)
        self.treeWidget.setItemWidget(self.topLevelItem, 1, self.multi)
        # Replacing the child items with widgets
        self.treeWidget.setItemWidget(self.childItems[0], 1, self.childButton_1)
        self.treeWidget.setItemWidget(self.childItems[1], 0, self.childButton_2)
        self.treeWidget.setItemWidget(self.childItems[2], 0, self.childButton_3)
        self.treeWidget.setItemWidget(self.childItems[3], 0, self.childLineEdit)
        # Connecting the widgets with corresponding slots
        self.topLevelButton.clicked.connect(self.top_button_clicked)
        self.childButton_1.clicked.connect(self.child_button_1_clicked)
        self.childButton_2.clicked.connect(self.child_button_2_clicked)
        self.childButton_3.clicked.connect(self.child_button_3_clicked)
        self.childLineEdit.textEdited.connect(self.child_lineedit_edited)
        # Setting the layout
        self.setWindowTitle("QTreeWidget with Button Example")
        self.setLayout(self.vboxLayout)

    # ............. (contd) ....... part-2

    # ........... (contd) ........... from part-2
    @pyqtSlot(bool)
    def top_button_clicked(self, clicked):
        self.label.setText("Top Level Button was Clicked")

    @pyqtSlot(bool)
    def child_button_1_clicked(self, clicked):
        self.label.setText("Child button 1 was clicked")

    @pyqtSlot(bool)
    def child_button_2_clicked(self, clicked):
        self.label.setText("Child button 2 was clicked")

    @pyqtSlot(bool)
    def child_button_3_clicked(self, clicked):
        self.label.setText("Child button 3 was clicked")

    @pyqtSlot("QString")
    def child_lineedit_edited(self, edited_text):
        self.label.setText(str(edited_text))


class MultiWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MultiWidget, self).__init__(parent)
        # self.setStyleSheet(
        #     "background-color:black; border:1px solid rgb(255, 170, 255);"
        # )
        # add your buttons
        layout = QHBoxLayout()

        # adjust spacings to your needs
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)

        # add your buttons
        layout.addWidget(QLabel("  Test: "))
        layout.addWidget(QLineEdit())
        button1 = QPushButton("Delete")
        button1.setGeometry(QtCore.QRect(10, 0, 91, 31))
        button1.setMinimumWidth(5)
        layout.addWidget(button1)
        layout.addWidget(QLabel("  Test: "))
        layout.addWidget(QLineEdit())
        button1 = QPushButton("Delete")
        button1.setGeometry(QtCore.QRect(10, 0, 91, 31))
        button1.setMinimumWidth(5)
        layout.addWidget(button1)
        layout.addWidget(QLabel("  Test: "))
        layout.addWidget(QLineEdit())
        button1 = QPushButton("Delete")
        button1.setGeometry(QtCore.QRect(10, 0, 91, 31))
        button1.setMinimumWidth(5)
        layout.addWidget(button1)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    treeWidgetDialog = TreeWidgetWithWidgetItems()
    treeWidgetDialog.show()
    sys.exit(app.exec_())
