from layout.forms.common import SingleForm
from PyQt5.QtWidgets import QRadioButton, QListWidget, QPushButton,  QFileDialog, QMessageBox
import ast


class NumbersEliminatorForm(SingleForm):
    def __init__(
        self, 
        whiteBallRadio: QRadioButton,
        goldBallRadio: QRadioButton,
        whiteBallList: QListWidget,
        goldBallList: QListWidget,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.whiteBallRadio = whiteBallRadio
        self.goldBallRadio = goldBallRadio
        self.whiteBallList = whiteBallList
        self.goldBallList = goldBallList
    
        self.whiteBallRadio.clicked.connect(lambda: self.toggleRadioBall("white"))
        self.goldBallRadio.clicked.connect(lambda: self.toggleRadioBall("gold"))
        self.whiteBallList.clicked.connect(lambda: self.toggleRadioBall("white"))
        self.goldBallList.clicked.connect(lambda: self.toggleRadioBall("gold"))

        self.plusBtn.disconnect()
        self.deleteBtn.disconnect()
        self.plusBtn.clicked.connect(self.addItemToBallList)
        self.deleteBtn.clicked.connect(self.deleteBallFromList)

    def toggleRadioBall(self, id: str ="white"):
        if id == "white":
            self.whiteBallRadio.setChecked(True)
            self.goldBallRadio.setChecked(False)
        if id == "gold":
            self.whiteBallRadio.setChecked(False)
            self.goldBallRadio.setChecked(True)
        
    def getCurrentBall(self):
        if self.whiteBallRadio.isChecked():
            return "white"
        if self.goldBallRadio.isChecked():
            return "gold"

    def addItemToBallList(self):
        currentBall = self.getCurrentBall()
        value = self.input.text()
        if len(value) < 1:
            return
        if currentBall == "white":
            self.whiteBallList.addItem(value)
        if currentBall == "gold":
            self.goldBallList.addItem(value)
    
    def deleteBallFromList(self):
        currentBall = self.getCurrentBall()
        if currentBall == "white":
            row = self.whiteBallList.currentRow()
            self.whiteBallList.takeItem(row)
        if currentBall == "gold":
            row = self.goldBallList.currentRow()
            self.goldBallList.takeItem(row)


class SumEliminatorForm(SingleForm):
    def __init__(self,sumBtn: QPushButton, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sumBtn = sumBtn


class ColumnRangesForm(SingleForm):
    def __init__(self, saveBtn: QPushButton, loadBtn: QPushButton, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saveBtn = saveBtn
        self.loadBtn = loadBtn

        self.saveBtn.clicked.connect(self.saveFile)
        self.loadBtn.clicked.connect(self.loadFile)
        
    def saveFile(self):
        messageBox = QMessageBox()
        messageBox.setText("Are you sure?")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        messageBox.exec_()
        print("hello")
        if messageBox.standardButton(messageBox.clickedButton()) == QMessageBox.Yes:
            values = [self.qlist.item(i).text() for i in range(self.qlist.count())]
            print("values: ", values)
            with open("results.txt", "w") as output:
                output.write(str(values))

    def loadFile(self):
        """Open a file using a Dialog window."""
        dlg = QFileDialog()
        filesFilter = "txt files(*.txt);; All files(*.*)"
        filepath = dlg.getOpenFileName(None, "Choose a directory", "", filesFilter)
        if len(filepath) > 0:
            file = filepath[0]
            data = []

            with open(file, "r") as f:
                for line in f:
                    _list = ast.literal_eval(line)
                    data.append(_list)

            if len(data) > 0:
                self.qlist.addItems(data[0])
