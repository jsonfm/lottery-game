from PyQt5.QtWidgets import QMainWindow
from layout.forms.common import SingleForm
from layout.forms.middle import NumbersEliminatorForm, SumEliminatorForm, ColumnRangesForm


class Middle:
    def __init__(self, parent: QMainWindow):
        for attr, value in parent.__dict__.items():
            setattr(self, attr, value)

        self.numbersEliminator = NumbersEliminatorForm(
            input=self.input21,
            plusBtn=self.plusBtn21,
            deleteBtn=self.deleteBtn21,
            whiteBallRadio=self.whiteBallRadio,
            goldBallRadio=self.goldBallRadio,
            whiteBallList=self.whiteBallList,
            goldBallList=self.goldBallList,
            qlist=None,
        )

        self.differenceColumn = SingleForm(
            input=self.input22,
            plusBtn=self.plusBtn22,
            deleteBtn=self.deleteBtn22,
            qlist=self.list22
        )

        self.sumEliminator = SumEliminatorForm(
            input=self.input23,
            plusBtn=self.plusBtn23,
            deleteBtn=self.deleteBtn23,
            qlist=self.list23,
            sumBtn=self.sumBtn23
        )

        self.pairEliminator = SingleForm(
            input=self.input24,
            plusBtn=self.plusBtn24,
            deleteBtn=self.deleteBtn24,
            qlist=self.list24,
        )

        self.eliminateSmaller = SingleForm(
            input=self.input25,
            plusBtn=self.plusBtn25,
            deleteBtn=self.deleteBtn25,
            qlist=self.list25,
        )

        self.columnRanges = ColumnRangesForm(
            input=self.input26,
            plusBtn=self.plusBtn26,
            deleteBtn=self.deleteBtn26,
            qlist=self.list26,
            saveBtn=self.saveBtn26,
            loadBtn=self.loadBtn26
        )