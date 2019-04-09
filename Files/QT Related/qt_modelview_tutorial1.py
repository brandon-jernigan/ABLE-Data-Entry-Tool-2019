from PyQT5 import QApplication
from PyQT5 import QTableView
import mymodel.py
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableView = QTableView()
    tableView = MyModel()
    tableView.setModel(myModel)
    tableView.show()
    sys.exit(app.exec_())
