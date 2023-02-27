import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtGui import QClipboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 創建一個PlainTextEdit
        self.textEdit = QPlainTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # 創建剪貼簿
        self.clipboard = QApplication.clipboard()

    def keyPressEvent(self, event):
        # 按下Ctrl+C時執行
        if event.matches(QApplication.keyboardModifiers() | Qt.Key.Key_C):
            # 取得目前滑鼠選取的文字
            selected_text = self.clipboard().text(QClipboard.Selection)

            # 將文字插入到PlainTextEdit中
            cursor = self.textEdit.textCursor()
            cursor.insertText(selected_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())