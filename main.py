import os
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from layout.upper import Upper
from layout.middle import Middle
from layout.lower import Lower, FinalLower


ui_path = os.path.dirname(os.path.abspath(__file__))
ui_file = os.path.join(ui_path, "gui", "main.ui")


class Lottery(QMainWindow):
    """A lottery app"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(ui_file, self)

        # Layout
        self.upper = Upper(self)
        self.middle = Middle(self)
        self.lower1 = Lower(self)
        self.lower2 = FinalLower(self)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_combination)

        # Events
        self.generateRandomBtn.clicked.connect(self.random)

    def random(self):
        self.timer.start(100)
    
    def update_combination(self):
        number = random.randint(80000, 100000)
        self.combinationLabel.setText(f"Combinations: {number}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Lottery()
    w.show()
    sys.exit(app.exec_())