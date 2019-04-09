l1 = QTreeWidgetItem(["String A", "", ""])
l2 = QTreeWidgetItem(["String AA", "", ""])
for i in range(3):
    l1_child = QTreeWidgetItem(
        ["Child A" + str(i), "Child B" + str(i), "Child C" + str(i)]
    )
    l1.addChild(l1_child)

for j in range(2):
    l2_child = QTreeWidgetItem(
        ["Child AA" + str(j), "Child BB" + str(j), "Child CC" + str(j)]
    )
    l2.addChild(l2_child)

self.tree_parameters.resize(500, 200)
self.tree_parameters.setColumnCount(3)
self.tree_parameters.setHeaderLabels(["Column 1", "Column 2", "Column 3"])
self.tree_parameters.addTopLevelItem(l1)
self.tree_parameters.addTopLevelItem(l2)


item = QTreeWidgetItem()
self.tree_parameters.addTopLevelItem(item)
widget = QSpinBox()
widget.setValue(5)
self.tree_parameters.setItemWidget(item, 1, widget)
