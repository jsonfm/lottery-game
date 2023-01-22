from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget


class SingleForm:
    def __init__(self, input: QLineEdit, plusBtn: QPushButton, deleteBtn: QPushButton, qlist: QListWidget):
        self.input = input
        self.plusBtn = plusBtn
        self.deleteBtn = deleteBtn
        self.qlist = qlist

        self.input.textChanged.connect(self.updateInputValue)
        self.plusBtn.clicked.connect(self.addItemToList)
        self.deleteBtn.clicked.connect(self.removeItemFromList)

    def updateInputValue(self, value):
        try:
            int(value)
        except:
            self.input.clear()
    
    def addItemToList(self):
        value = self.input.text()
        if len(value) > 0:
            self.qlist.addItem(value)

    def removeItemFromList(self):
        row = self.qlist.currentRow()
        self.qlist.takeItem(row)