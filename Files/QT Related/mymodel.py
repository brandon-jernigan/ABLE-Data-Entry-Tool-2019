from pyQT5 import QAbstractTableModel

class MyModel(QAbstractTableModel)

    MyModel(QObject *parent = nullptr);
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

class MyModel(QAbstractTableModel)
    def __init__(self):
        super(MyModel, self).__init__()
        self.rowCount(QModelIndex())
        self.columnCount(QModelIndex())
        data = QVariant(QModelIndex, role = QT.DisplayRole)