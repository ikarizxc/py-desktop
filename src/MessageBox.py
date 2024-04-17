from PySide6.QtWidgets import QMessageBox


class MessageBox(QMessageBox):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(QMessageBox.Information)