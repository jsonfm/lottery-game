import re
from PyQt5.QtWidgets import (
    QRadioButton, 
    QListWidget, 
    QPushButton, 
    QLineEdit, 
    QCheckBox, 
    QErrorMessage,
)
from layout.forms.common import SingleForm
from layout.errors.dialog import showErrorDialog


class CombinationsRangeForm(SingleForm):
    def __init__(
        self, 
        beforeInput: QLineEdit,
        afterInput: QLineEdit,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)


class EvenOddForm(SingleForm):
    def __init__(
        self, 
        evenBtn: QPushButton,
        oddBtn: QPushButton,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.evenBtn = evenBtn
        self.oddBtn = oddBtn

        self.evenBtn.clicked.connect(self.allEven)
        self.oddBtn.clicked.connect(self.allOdd)

    def updateInputValue(self, value):
        ...

    def addItemToList(self):
        value = self.input.text()
        pattern =  r'^\d+(,\s?\d+){5}$' # number,number,number,number,number,number
        pattern = r'^[EO],[EO],[EO],[EO],[EO],[EO]$' # E/O,E/O,E/O,E/O,E/O,E/O
        match = re.match(pattern, value)
        if not match:
            showErrorDialog('Enter a pattern of six E/O separated by comma. e.g. E,O,O,E,E,E')
            return
        if len(value) > 0:
            self.qlist.addItem(value)

    def allEven(self):
        item = ('E,' * 6)[:-1]
        self.qlist.clear()
        self.qlist.addItem(item)

    def allOdd(self):
        item = ('O,' * 6)[:-1]
        self.qlist.clear()
        self.qlist.addItem(item)

class ColumnPatternForm(SingleForm):
    def __init__(
        self, 
        colorCheckbox: QCheckBox,
        threeConsecutivesCheckbox: QCheckBox,
        checkTwoCheckBox: QCheckBox,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)


class ColumnPatternSumForm(SingleForm):
    def __init__(
        self, 
        colorCheckbox: QCheckBox,
        threeConsecutivesCheckbox: QCheckBox,
        checkTwoCheckBox: QCheckBox,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)
