from layout.forms.common import SingleForm
from PyQt5.QtWidgets import QRadioButton, QListWidget, QPushButton, QLineEdit, QCheckBox


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
