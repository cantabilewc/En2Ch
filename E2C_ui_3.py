
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt,QRect

class MainWindow(QMainWindow):
    def __init__(self):
        # super().__init__()呼叫了QMainWindow這個父類別的建構函式，這樣我們才能在自己的子類別中使用QMainWindow提供的方法和屬性。
        super().__init__()
        self.centralwidget = QPlainTextEdit()
        self.resize(500, 500)
        # 創建一個PlainTextEdit
        # self.plainTextEdit = QPlainTextEdit()
        self.centralwidget.setGeometry(QRect(40, 120, 301, 121))
        self.setCentralWidget(self.centralwidget)
        # self.textEdit = QPlainTextEdit(self)
        # self.setCentralWidget(self.textEdit)
        # 創建剪貼簿
        self.clipboard = QApplication.clipboard()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.plainTextEdit.setPlainText(self.clipboard.text())

if __name__ == '__main__':
    app = QApplication([])
    Mywindow = MainWindow()
    Mywindow.show()
    app.exec_()