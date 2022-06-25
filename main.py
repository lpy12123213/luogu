import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
from bs4 import BeautifulSoup
import re,os
from PyQt5.QtGui import QTextCursor
url__ = "https://www.luogu.com.cn/problem/"

def geshihua(text):
    bs = BeautifulSoup(text, "html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>", "# ", md)
    md = re.sub("<h2>", "## ", md)
    md = re.sub("<h3>", "#### ", md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)
    return md
def do(p, i):
    save_data = os.getcwd()+r'\luogu\problem'+'\\'
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
    # }
    save_data+=p+'\\'
    try:
        os.mkdir(save_data)
    except:
        pass
    u=url__+p
    response = requests.get(f'https://www.luogu.com.cn/problem/{p}{i}', headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
    })
    try:
        response.raise_for_status()
    except:
        return f"啊哦，网站成了{str(response)}了"
    html = response.text
    response.close()
    # print(html)
    if "Exception" not in html:  # 洛谷中没找到该题目或无权查看的提示网页中会有该字样
        problemMD = f'[到达网站]({u+str(i)})'+(geshihua(html))
        with open(f"{save_data}{p}{i}.md", "w", encoding="utf-8") as f:
            f.write(problemMD)
        print(f"爬取题目{p}{i}完毕")
        return f"爬取题目{p}{i}完毕"
    else:
        print("error")
        return "error"


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(821, 473)
        Widget.setStyleSheet("")
        self.leixin = QtWidgets.QLineEdit(Widget)
        self.leixin.setGeometry(QtCore.QRect(400, 50, 241, 25))
        self.leixin.setFrame(False)
        self.leixin.setObjectName("leixin")
        self.out = QtWidgets.QTextEdit(Widget)
        # self.out.setEnabled(False)
        self.out.setGeometry(QtCore.QRect(160, 250, 481, 171))
        # self.out.setMouseTracking(True)
        # self.out.setAcceptDrops(True)
        # self.out.setTabChangesFocus(False)
        self.out.setReadOnly(True)
        # self.out.setOverwriteMode(False)
        # self.out.moveCursor(QTextCursor.End)
        self.out.setObjectName("out")
        self.gridLayoutWidget = QtWidgets.QWidget(Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(159, 100, 481, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.start = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.start.setFrame(False)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)
        self.end = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.end.setFrame(False)
        self.end.setObjectName("end")
        self.gridLayout.addWidget(self.end, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(550, 200, 93, 29))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 231, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 231, 21))
        self.label_4.setObjectName("label_4")
        self.clean = QtWidgets.QPushButton(Widget)
        self.clean.setGeometry(QtCore.QRect(650, 390, 93, 29))
        self.clean.setFlat(True)
        self.clean.setObjectName("clean")
        self.pushButton.clicked.connect(self.main)
        self.clean.clicked.connect(self.out.clear)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "开始区间"))
        self.label_2.setText(_translate("Widget", "结束区间"))
        self.pushButton.setText(_translate("Widget", "确定"))
        self.label_3.setText(_translate("Widget", "题目类型（是P、SP等等）"))
        self.label_4.setText(_translate("Widget", "就只是一个简简单单的洛谷爬行器"))
        self.clean.setText(_translate("Widget", "清除"))
    def main(self):
        def do_():
            p = self.leixin.text()
            try:
                s = int(self.start.text())
                e = int(self.end.text())
            except ValueError:
                self.out.append('A~O~输入的开始与结束不可以是string类哦！')
            else:
                for i in range(s, e+1):
                    self.out.append(do(p, i))
                self.out.append('爬取完毕')
        t0ob=threading.Thread(target=do_)
        t0ob.start()
        # t0ob.join()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Widget()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
