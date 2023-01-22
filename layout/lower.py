from PyQt5.QtWidgets import QMainWindow
from layout.forms.common import SingleForm
from layout.forms.lower import CombinationsRangeForm, EvenOddForm, ColumnPatternForm
from layout.forms.middle import ColumnRangesForm


class Lower:
    """Lower Row"""
    def __init__(self, parent: QMainWindow):
        for attr, value in parent.__dict__.items():
            setattr(self, attr, value)

        self.combinationsRangeEliminator = CombinationsRangeForm(
            beforeInput=self.beforeInput,
            afterInput=self.afterInput,
            input=self.input31,
            plusBtn=self.plusBtn31,
            deleteBtn=self.deleteBtn31,
            qlist=self.list31
        )

        self.evenOddPattern = EvenOddForm(
            evenBtn=self.evenBtn32,
            oddBtn=self.oddBtn32,
            input=self.input32,
            plusBtn=self.plusBtn32,
            deleteBtn=self.deleteBtn32,
            qlist=self.list32,
        )

        self.columnPattern = ColumnPatternForm(
            colorCheckbox=self.check331,
            threeConsecutivesCheckbox=self.check332,
            checkTwoCheckBox=self.check333,
            input=self.input33,
            plusBtn=self.plusBtn33,
            deleteBtn=self.deleteBtn33,
            qlist=self.list33
        )

        self.secondDigitEliminator = SingleForm(
            input=self.input34,
            plusBtn=self.plusBtn34,
            deleteBtn=self.deleteBtn34,
            qlist=self.list34
        )

        self.combinationChecker = SingleForm(
            input=self.input35,
            plusBtn=self.plusBtn35,
            deleteBtn=self.deleteBtn35,
            qlist=self.list35
        )

        self.nextNumberSum = ColumnRangesForm(
            saveBtn=self.saveBtn36,
            loadBtn=self.loadBtn36,
            input=self.input36,
            plusBtn=self.plusBtn36,
            deleteBtn=self.deleteBtn36,
            qlist=self.list36
        )


class FinalLower:
    """"Final Lower Row"""
    def __init__(self, parent: QMainWindow):
        for attr, value in parent.__dict__.items():
            setattr(self, attr, value)

        self.lessThan = SingleForm(
            input=self.input41,
            plusBtn=self.plusBtn41,
            deleteBtn=self.deleteBtn41,
            qlist=self.list41
        )

        self.sumEliminator = SingleForm(
            input=self.input42,
            plusBtn=self.plusBtn42,
            deleteBtn=self.deleteBtn42,
            qlist=self.list42
        )

        self.numberFinder = SingleForm(
            input=self.input44,
            plusBtn=self.plusBtn44,
            deleteBtn=self.deleteBtn44,
            qlist=self.list44
        )

        self.multiNumberFinder = SingleForm(
            input=self.input45,
            plusBtn=self.plusBtn45,
            deleteBtn=self.deleteBtn45,
            qlist=self.list45
        )
