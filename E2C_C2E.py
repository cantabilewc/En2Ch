from PyQt5 import QtCore, QtGui, QtWidgets

import requests
import itertools
import opencc # If you add the directory containing the opencc module to the PYTHONPATH environment variable, Python will search for the opencc module in that directory and its subdirectories. When you import opencc, Python will find the module in the opencc directory and load it into memory.


# 在這裡，Ui_MainWindow 這個類別是繼承自 object，因為在定義 Ui_MainWindow 的時候，
# 括號內的 object 表示繼承自 object 這個基底類別。不過，這其實是可以省略的，
# 因為在 Python 3 中，所有的類別都會自動繼承自 object，所以可以簡化為 class Ui_MainWindow:。
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.font = QtGui.QFont('Yu Gothic Medium', 9)
        self.font_ja = QtGui.QFont('Yu Gothic Medium', 9)
        self.font_ch = QtGui.QFont('微軟正黑體', 9)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(225, 40, 111, 61))

        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startTranslating)
        self.startFlag = [False]  # 將 startFlag 變數宣告為一個 List然後在建立 CopyPlainTextEdit 物件的時候傳遞這個 List。這樣在 mousePressEvent 中就可以透過這個 List 存取到 startFlag 變數，並進行修改。
        self.pushButton.setFont(self.font)
        # fontDB = QtGui.QFontDatabase()
        # for fontFamily in fontDB.families():
        #     print(fontFamily)
        
        # Label
        self.text1 = QtWidgets.QLabel("From", self.centralwidget)
        self.text1.setGeometry(40, 40, 30, 20)
        self.text1.setFont(self.font)
        self.text1.setObjectName("FROM")
        self.text2 = QtWidgets.QLabel("To", self.centralwidget)
        self.text2.setGeometry(40, 80, 30, 20)
        self.text2.setObjectName("TO")
        self.text2.setFont(self.font)
        
        # ComboBox
        choices = ['auto', 'zh-TW', 'en', 'ja']
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(80, 40, 60, 20))
        self.comboBox1.addItems(choices)
        self.comboBox1.setCurrentIndex(0)
        self.sl = [choices[0]]
        self.comboBox1.setObjectName("SL")
        self.comboBox1.currentIndexChanged.connect(self.handle_selection_change)
        self.comboBox1.setFont(self.font)
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(80, 80, 60, 20))
        self.comboBox2.addItems(choices)
        self.comboBox2.setCurrentIndex(1)
        self.tl = [choices[1]] # default translate to TW
        self.comboBox2.setObjectName("TL")
        self.comboBox2.currentIndexChanged.connect(self.handle_selection_change)
        self.comboBox2.setFont(self.font)

        # setGeometry是所有继承自QWidget的类（例如QPlainTextEdit）都拥有的方法。在这里，
        # CopyPlainTextEdit作为QPlainTextEdit的子类，自然也具有该方法，所以可以在CopyPlainTextEdit对象上调用setGeometry方法。
        self.plainTextEdit_result = QtWidgets.QPlainTextEdit(self.centralwidget) #parent 
        self.plainTextEdit_result.setGeometry(QtCore.QRect(40, 250, 500, 121))
        self.plainTextEdit_result.setFont(self.font_ch)
        self.plainTextEdit_result.setObjectName("translating result")

        self.plainTextEdit = CopyPlainTextEdit(self.centralwidget, self.startFlag, self.plainTextEdit_result, self.sl, self.tl) # parent object, and arguments
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 120, 500, 121))
        self.plainTextEdit.setFont(self.font)

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

    def handle_selection_change(self):
        self.sl[0] = self.comboBox1.currentText()
        self.tl[0] = self.comboBox2.currentText()
        if self.sl[0] == 'ja':
            self.plainTextEdit.setFont(self.font_ja)
        elif self.sl[0] == 'zh-TW':
            self.plainTextEdit.setFont(self.font_ch)
        else:
            self.plainTextEdit.setFont(self.font)

        if self.tl[0] == 'ja':
            self.plainTextEdit_result.setFont(self.font_ja)
        elif self.tl[0] == 'zh-TW':
            self.plainTextEdit_result.setFont(self.font_ch)
        else:
            self.plainTextEdit_result.setFont(self.font)
        # print(self.sl,self.tl)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E2C C2E"))
        self.pushButton.setText(_translate("MainWindow", "Start Translating"))

    def startTranslating(self):
        self.startFlag[0] = not self.startFlag[0]
        if self.startFlag[0]:
            self.pushButton.setText("Translating")
        else:
            self.pushButton.setText("Start Translating")

# 在这个代码中，括号里的参数是用来指定 PlainTextEdit 类的父类或基类的，
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
# The parent parameter in def __init__ and the parent parameter in super().__init__ refer to different objects.
# In def __init__, parent is a parameter passed to the constructor of the CopyPlainTextEdit class. It is used to set the parent widget of the CopyPlainTextEdit widget.
# In super().__init__, parent is also a parameter passed to the constructor of the parent class of CopyPlainTextEdit, which is QPlainTextEdit. It is used to set the parent widget of the QPlainTextEdit widget.
class CopyPlainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None, startFlag=None, plainTextEdit_result=None, source_language = None, target_language = None): # 在 Python 中，None 是一個特殊的值，表示沒有值或空值。在這個程式碼中，None 被用來指定函數參數的預設值。在 __init__ 函數中，parent 參數預設值為 None，這意味著如果你不給這個參數傳遞任何值，它就會使用 None 作為預設值。同樣地，startFlag 和 plainTextEdit_result 參數的預設值也是 None，這意味著如果你不給這些參數傳遞任何值，它們也會使用 None 作為預設值。
        super().__init__(parent=parent)#def __init__(self, parent=None, startFlag=None, plainTextEdit_result=None, source_language=None, target_language=None)中的parent是CopyPlainTextEdit的父級窗口，用於將CopyPlainTextEdit添加到視窗中的特定部件（例如，在QWidget上）。在這種情況下，parent參數通常用於將視窗元素組織成層次結構。super().__init__(parent=parent)調用父類QPlainTextEdit的構造函數，其中的parent也是指定CopyPlainTextEdit的父級窗口。簡而言之，這兩個parent是指不同的東西，def __init__中的parent指CopyPlainTextEdit的父級窗口，而super().__init__(parent=parent)中的parent指QPlainTextEdit的父級窗口。
        self.setReadOnly(True)
        self.setObjectName("plainTextEdit")
        self.startFlag = startFlag  # 在建立物件時將 startFlag 變數的 List 存下來
        self.plainTextEdit_result = plainTextEdit_result
        self.source_language = source_language
        self.target_language = target_language

# 在 PyQt5 中，如果要处理某种类型的事件，通常需要使用对应的事件处理方法，
# 并按照 PyQt5 事件处理机制的规范命名，例如 mousePressEvent，keyPressEvent 等等。
# 这些事件处理方法都有一个固定的参数，即 event，它是 PyQt5 中的事件对象，包含了事件的相关信息。
# 这个参数名是固定的，不能改变。因此，如果你想处理某种类型的事件，需要按照规范编写相应的事件处理方法，
# 并正确处理 event 参数中的事件信息。但是，如果你在自己的函数中使用了 event 作为参数名，
# 这并不会使这个函数成为一个事件处理方法。
# 在这个函数中，event 参数只是一个普通的参数名，你需要自己处理这个参数并在函数中使用它。

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.startFlag[0]:
            clipboard = QtWidgets.QApplication.clipboard()
            text = clipboard.text()
            if not text:
                return
            self.setPlainText(text)
            self.translate_text_POST(text)

    def translate_text_POST(self, text):
        url = 'https://translate.google.com/translate_a/single' # 是 Google 翻譯的網頁版介面，它是一個非正式的 API 端點，用於網頁界面的自動翻譯，與 Google Translate API 並不相同。 當您在 Google 翻譯的頁面按下 F12 並執行翻譯時，您看到的 URL 可能與 Google Translate API 不同。這是因為 Google 翻譯的網頁版介面使用了不同的技術和端點來實現翻譯功能。這些端點可能不是公開的 API，也可能隨時更改。
        params = {
            'client': 'gtx', # use 'webapp' leading to the 403 error response
            'sl': self.source_language[0],  # source language (auto-detect)
            'tl': self.target_language[0],  # target language (Traditional Chinese)
            'hl': 'en',  # interface language (English)
            'dt': ['t', 'at'],  # response format: text and alternative translations
            'dj': '1',  # response format: JSON
            'source': 'input',  # source of the translation: input field
            'q': text,  # text to be translated
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Referer': 'https://translate.google.com/',
        }

        response = requests.post(url, headers=headers, params=params) # A 403 Forbidden response usually indicates that the server understood your request, but is refusing to fulfill it, usually because the client does not have the necessary permissions to access the requested resource.

        result = response.json()
        # print('\n')
        trans_list = []
        for item in result['sentences']:
            # print(item['trans'])
            trans_list.append(item['trans'])
        translation = '\n'.join(trans_list)
        self.plainTextEdit_result.setPlainText(translation)

    def translate_text_GET(self, text):
        # Specify the URL and parameters for the request
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "auto",
            "tl": "zh-TW",
            "dt": "t",
            "q": text
        }

        # Send the request and get the response
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the response and get the translation
        translation = response.json() #[0][0][0]
        print('\n')
        print(translation)
        # self.plainTextEdit_result.setPlainText(translation)

    def translate_text_youdoa(self, text): # this private translation api sucks
        
        # url = 'https://dict.youdao.com/webtranslate' //這個是新的url，有加密過需解密，https://blog.csdn.net/Mr_blueD/article/details/90581634
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # 這個 URL 是通过在浏览器中使用开发者工具查看网络请求而获得的。在打开有道翻译官网后，使用开发者工具，可以看到请求的 URL，这个 URL 就是请求翻译结果的 URL。这个 URL 是可以使用 HTTP 或 HTTPS 协议的，只需要将请求的方式设置为 POST 就可以。而 URL https://fanyi.youdao.com/index.html# 是有道翻译官网的主页，不是请求翻译结果的 URL。虽然可以在该网页中输入文本并点击翻译按钮，但这个过程涉及到浏览器的 JavaScript 代码，不方便用 Python 直接模拟。
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        # 根據程式碼中的 data 參數設定，翻譯的API使用了 "FY_BY_REALTIME" 的 action，這表示它是一個即時翻譯的請求，只能翻譯一個句子，並且忽略後面的內容。如果想要翻譯多個句子，需要使用其他選項，例如 "FY_BY_CLICKBUTTION"，這可以讓API知道在請求中翻譯的是多個句子。你可以修改 data 中的 action 屬性，以便翻譯多個句子。此外，請注意，翻譯的結果是以 JSON 格式返回的，因此需要對結果進行解析以提取所需的翻譯內容
        data = {
            'i': text,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            # 'salt': '1534741252894',
            # 'sign': '1c2e58f79a8362e4a7b44cdd67a1a9c8',
            # salt和sign在此程式碼中是有固定的值，是因為網頁前端的JavaScript程式碼是固定的，透過JavaScript計算得到的。這些值固定下來，就可以在發送請求時直接寫在data參數中。但是這些值可能會有改變，這時候你的程式就會無法取得正確的回應，因此如果需要長期使用這個程式，最好還是能夠找到計算這些值的方法，並將其寫入程式中。
            #         function La(e) {
            #           const t = Va(navigator.appVersion)
            #           , o = "" + (new Date).getTime()
            #           , n = o + parseInt(10 * Math.random(), 10)
            #           , a = Va(_a + e + n + Na);
            #               return {
            #                    ts: o,
            #                    bv: t,
            #                   salt: n,
            #                   sign: a
            #               }
            #         }
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        }
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        # print(result)
        flattened_lst = list(itertools.chain.from_iterable(result['translateResult']))
        tgt_str = ''
        for translation in flattened_lst:
            tgt_str += translation['tgt'] # dictionary搜尋法
            tgt_str += '\n'

        converter = opencc.OpenCC('s2twp') # In the above example, s2twp.json is a conversion configuration file that specifies how to convert Simplified Chinese to Traditional Chinese with Taiwan standard. You can use other configuration files to convert between different standards, such as Hong Kong, Macau, or Mainland China.
        traditional_text = converter.convert(tgt_str)
        # print(tgt_str)  
        # translation = '\n'.join(translation)  # 將列表轉換為字符串，每個元素之間用換行符分隔
        self.plainTextEdit_result.setPlainText(traditional_text)


if __name__ == "__main__": # if other scripts import the functions above, this line will not be executed
    import sys # for the exit function
    app = QtWidgets.QApplication(sys.argv) # if there are command lines arguments to be sent to the QApplication
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())