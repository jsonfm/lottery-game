from PyQt5.QtWidgets import QMessageBox


def showErrorDialog(message: str = "something is wrong!"):
    """Shows a Dialog Window."""
    error = QMessageBox()
    error.setText(message)
    error.exec_()