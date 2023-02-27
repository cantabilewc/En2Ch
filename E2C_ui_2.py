from PyQt5.QtWidgets import QApplication, QPlainTextEdit
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt

class PlainTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            clipboard = QApplication.clipboard()
            self.setPlainText(clipboard.text())

if __name__ == '__main__':
    app = QApplication([])
    plainTextEdit = PlainTextEdit()
    plainTextEdit.show()
    app.exec_()