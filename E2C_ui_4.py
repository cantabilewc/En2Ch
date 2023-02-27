from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup

#在這裡，Ui_MainWindow 這個類別是繼承自 object，因為在定義 Ui_MainWindow 的時候，
# 括號內的 object 表示繼承自 object 這個基底類別。不過，這其實是可以省略的，
# 因為在 Python 3 中，所有的類別都會自動繼承自 object，所以可以簡化為 class Ui_MainWindow:。
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 40, 111, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startTranslating)
        self.startFlag = [False]  # 將 startFlag 變數宣告為一個 List然後在建立 CopyPlainTextEdit 物件的時候傳遞這個 List。這樣在 mousePressEvent 中就可以透過這個 List 存取到 startFlag 變數，並進行修改。

#setGeometry是所有继承自QWidget的类（例如QPlainTextEdit）都拥有的方法。在这里，
# CopyPlainTextEdit作为QPlainTextEdit的子类，自然也具有该方法，所以可以在CopyPlainTextEdit对象上调用setGeometry方法。
        self.plainTextEdit = CopyPlainTextEdit(self.centralwidget, self.startFlag) #parent object, and argument
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 120, 301, 121))
        # self.plainTextEdit.setObjectName("plainTextEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Translating"))

    def startTranslating(self):
        self.startFlag[0] = not self.startFlag[0]
        if self.startFlag[0]:
            self.pushButton.setText("Translating")
        else:
            self.pushButton.setText("Start Translating")

#在这个代码中，括号里的参数是用来指定 PlainTextEdit 类的父类或基类的，
# 它告诉 PyQt5 PlainTextEdit 继承了 QtWidgets.QPlainTextEdit 类的所有属性和方法，
# 使得 PlainTextEdit 可以使用 QtWidgets.QPlainTextEdit 中的所有函数和变量。
# 通过继承 QtWidgets.QPlainTextEdit 类，可以在这个基础上扩展和自定义控件的功能。

# The CopyPlainTextEdit class is a subclass of the QPlainTextEdit class and overrides the mousePressEvent method. 
# This method detects when the left mouse button is clicked and reads the text in the clipboard. 
# The text in the clipboard is then set as the text of the custom widget.
# CopyPlainTextEdit 是一個自定義的 QtWidgets.QPlainTextEdit 的子類別，
# 
# 用於創建一個新的多行純文本編輯框，其 __init__ 方法中的 super() 函數
# 調用了父類別 QtWidgets.QPlainTextEdit 的 __init__ 方法，
# 通過 parent 參數設置了其父視窗（在這個例子中，父視窗為 Ui_MainWindow 中的 centralwidget）。
# 這樣做的目的是繼承了父類別中的屬性和方法，同時在此基礎上進行自定義的修改和擴展。
# 
# 在定義 __init__ 函式時，可以為函式加入參數以接受外部傳入的參數，此處的 parent 即是繼承關係中的父類別，
# 用於在建立該物件時指定父物件，使得該物件成為父物件的子物件。
# 在上述程式碼中， parent=None 是在定義該函式時所設置的預設參數，
# 即若在建立物件時未給定該參數，則 parent 會預設為 None，表示該物件沒有父物件，
# 並可獨立存在。若有需要，則可在建立物件時透過指定 parent 參數的方式指定父物件，使得該物件成為該父物件的子物件。
class CopyPlainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None, startFlag=None):
        super().__init__(parent=parent)
        self.setReadOnly(True)
        self.setObjectName("plainTextEdit")
        self.startFlag = startFlag  # 在建立物件時將 startFlag 變數的 List 存下來

#在 PyQt5 中，如果要处理某种类型的事件，通常需要使用对应的事件处理方法，
# 并按照 PyQt5 事件处理机制的规范命名，例如 mousePressEvent，keyPressEvent 等等。
# 这些事件处理方法都有一个固定的参数，即 event，它是 PyQt5 中的事件对象，包含了事件的相关信息。
# 这个参数名是固定的，不能改变。因此，如果你想处理某种类型的事件，需要按照规范编写相应的事件处理方法，
# 并正确处理 event 参数中的事件信息。但是，如果你在自己的函数中使用了 event 作为参数名，
# 这并不会使这个函数成为一个事件处理方法。
# 在这个函数中，event 参数只是一个普通的参数名，你需要自己处理这个参数并在函数中使用它。

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.startFlag[0]:  # 存取 startFlag 變數的 List
            clipboard = QtWidgets.QApplication.clipboard()
            # 取得剪貼簿中的文字
            self.setPlainText(clipboard.text())
            # 網站的 URL
            # URL = 'https://fanyi.youdao.com/'
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            data = {
                'i': clipboard.text(),
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': '1534741252894',
                'sign': '1c2e58f79a8362e4a7b44cdd67a1a9c8',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_REALTIME',
                'typoResult': 'false'
            }
            response = requests.post(url, headers=headers, data=data)
            result = response.json()
            translation = result['translateResult'][0][0]['tgt']

            # 將翻譯後的文字顯示在螢幕上
            print(translation)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())