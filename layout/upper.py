from PyQt5.QtWidgets import QMainWindow
from layout.forms.common import SingleForm


class Upper:
    def __init__(self, parent: QMainWindow):
        for attr, value in parent.__dict__.items():
            setattr(self, attr, value)

        self.outRangeEliminator = SingleForm(
            input=self.input12,
            plusBtn=self.plusBtn12,
            deleteBtn=self.deleteBtn12,
            qlist=self.list12,
        )

        self.similarPairEliminator = SingleForm(
            input=self.input13,
            plusBtn=self.plusBtn13,
            deleteBtn=self.deleteBtn13,
            qlist=self.list13,
        )

        self.columnPairEliminator = SingleForm(
            input=self.input14,
            plusBtn=self.plusBtn14,
            deleteBtn=self.deleteBtn14,
            qlist=self.list14,
        )

        self.eliminateGreaterNumbers = SingleForm(
            input=self.input15,
            plusBtn=self.plusBtn15,
            deleteBtn=self.deleteBtn15,
            qlist=self.list15,
        )

        self.sumPosition = SingleForm(
            input=self.input16,
            plusBtn=self.plusBtn16,
            deleteBtn=self.deleteBtn16,
            qlist=self.list16,
        )