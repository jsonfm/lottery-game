from PyQt5.QtWidgets import QMessageBox


def showErrorDialog(message: str = "something is wrong!"):
    error = QMessageBox()
    error.setText(message)
    error.exec_()