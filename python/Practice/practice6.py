import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #라벨 1번 글자 및 위치 정의
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        #라벨 2번 글자 및 위치 정의
        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)

        #라벨1에 사용될 폰트 정의
        font1 = label1.font()
        font1.setPointSize(20)

        #라벨2에 사용될 폰트 및 두께 정의
        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        #폰트와 라벨 연결하기
        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())