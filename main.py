import os
from untitled import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Rabota_ne_wolk(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.button.clicked.connect(self.event_click)

    def event_click(self):
        text = self.line_way.text()
        os.chdir(text)
        for i in os.listdir():
            if '.webp' in i:
                os.rename(i[:len(i) - 5], i + '.jpeg')
                # print(i) debug


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Rabota_ne_wolk()
    w.show()
    sys.exit(app.exec_())
