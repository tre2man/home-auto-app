import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtSerialPort, QtCore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pymysql.cursors
from datetime import datetime, timedelta

class IOTMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle('IOT_Monitor')

    def MainUI(self):
        # tabs라는 q탭위셋 선언 후 탭1과 탭2 추가
        self.tabs = QTabWidget()
        self.tabs.addTab(self.SerialUI(), 'Count')
        self.tabs.addTab(self.GraphUI(), 'Graph')

        #박스 레이아웃에 q탭위젯 올리기 및 최종 레이아웃 저장
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)

    def SerialUI(self):
        # 1번 탭 코드
        self.tab1En = QWidget() #전체 레이아웃 설정
        self.tab1En.layout = QVBoxLayout(self) #VBox 레이아웃 선언
        self.tab1 = QWidget()  # q위젯 형태의 탭 선언
        self.tab1.layout = QGridLayout(self)  # q위젯 형태의 탭 선언

        # 시리얼통신 연결하는 버튼
        self.Connect = QPushButton('Connect')
        self.Connect.clicked.connect(self.ConnectSerial)

        # 결과값 출력하는 텍스트 및 텍스트 사이즈
        CountFontSize = 40
        self.textLivingroom = QLabel('0', self)
        fontLivingRoom = self.textLivingroom.font()
        fontLivingRoom.setPointSize(CountFontSize)
        self.textLivingroom.setFont(fontLivingRoom)

        self.textRoom1 = QLabel('0', self)
        fontRoom1 = self.textRoom1.font()
        fontRoom1.setPointSize(CountFontSize)
        self.textRoom1.setFont(fontRoom1)

        self.textRoom2 = QLabel('0', self)
        fontRoom2 = self.textRoom2.font()
        fontRoom2.setPointSize(CountFontSize)
        self.textRoom2.setFont(fontRoom2)

        self.textToilet = QLabel('0', self)
        fontToilet = self.textToilet.font()
        fontToilet.setPointSize(CountFontSize)
        self.textToilet.setFont(fontToilet)

        self.textWater = QLabel('0', self)
        fontWater = self.textWater.font()
        fontWater.setPointSize(CountFontSize)
        self.textWater.setFont(fontWater)

        self.textPIR = QLabel('0', self)
        fontPIR = self.textPIR.font()
        fontPIR.setPointSize(CountFontSize)
        self.textPIR.setFont(fontPIR)

        self.textGas = QLabel('0', self)
        fontGas = self.textLivingroom.font()
        fontGas.setPointSize(CountFontSize)
        self.textGas.setFont(fontGas)

        self.textBathroom = QLabel('0', self)
        fontBathroom = self.textLivingroom.font()
        fontBathroom.setPointSize(CountFontSize)
        self.textBathroom.setFont(fontBathroom)

        self.test = QLabel('0', self)
        fontest= self.test.font()
        fontest.setPointSize(20)
        self.test.setFont(fontest)

        #박스 변수 선언 및 텍스트 크기 조정
        boxFontSize = 20
        boxLivingRoom = QGroupBox('LivingRoom')
        fontboxLivingRoom = boxLivingRoom.font()
        fontboxLivingRoom.setPointSize(boxFontSize)
        boxLivingRoom.setFont(fontboxLivingRoom)

        boxRoom1 = QGroupBox('Room1')
        fontboxRoom1 = boxRoom1.font()
        fontboxRoom1.setPointSize(boxFontSize)
        boxRoom1.setFont(fontboxRoom1)

        boxRoom2 = QGroupBox('Room2')
        fontboxRoom2 = boxRoom2.font()
        fontboxRoom2.setPointSize(boxFontSize)
        boxRoom2.setFont(fontboxRoom2)

        boxToilet = QGroupBox('Toilet')
        fontboxToilet = boxToilet.font()
        fontboxToilet.setPointSize(boxFontSize)
        boxToilet.setFont(fontboxToilet)

        boxWater = QGroupBox('Water')
        fontboxWater = boxWater.font()
        fontboxWater.setPointSize(boxFontSize)
        boxWater.setFont(fontboxWater)

        boxPIR = QGroupBox('PIR')
        fontboxPIR = boxPIR.font()
        fontboxPIR.setPointSize(boxFontSize)
        boxPIR.setFont(fontboxPIR)

        boxGas = QGroupBox('Gas')
        fontboxGas = boxGas.font()
        fontboxGas.setPointSize(boxFontSize)
        boxGas.setFont(fontboxGas)

        boxBathroom = QGroupBox('Bathroom')
        fontboxBathroom = boxBathroom.font()
        fontboxBathroom.setPointSize(boxFontSize)
        boxBathroom.setFont(fontboxBathroom)

        #박스 안에 텍스트 넣기
        vbox1 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox1.addWidget(self.textLivingroom)
        boxLivingRoom.setLayout(vbox1)

        vbox2 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox2.addWidget(self.textRoom1)
        boxRoom1.setLayout(vbox2)

        vbox3 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox3.addWidget(self.textRoom2)
        boxRoom2.setLayout(vbox3)

        vbox4 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox4.addWidget(self.textToilet)
        boxToilet.setLayout(vbox4)

        vbox5 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox5.addWidget(self.textWater)
        boxWater.setLayout(vbox5)

        vbox6 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox6.addWidget(self.textPIR)
        boxPIR.setLayout(vbox6)

        vbox7 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox7.addWidget(self.textGas)
        boxGas.setLayout(vbox7)

        vbox8 = QBoxLayout(QBoxLayout.LeftToRight, self)
        vbox8.addWidget(self.textBathroom)
        boxBathroom.setLayout(vbox8)

        #탭1 레이아웃 조립하기
        self.tab1.layout.addWidget(self.Connect, 0, 3)
        self.tab1.layout.addWidget(boxLivingRoom, 1, 0)
        self.tab1.layout.addWidget(boxRoom1, 1, 1)
        self.tab1.layout.addWidget(boxRoom2, 1, 2)
        self.tab1.layout.addWidget(boxToilet, 1, 3)
        self.tab1.layout.addWidget(boxWater, 2, 0)
        self.tab1.layout.addWidget(boxPIR, 2, 1)
        self.tab1.layout.addWidget(boxGas, 2, 2)
        self.tab1.layout.addWidget(boxBathroom, 2, 3)
        self.tab1.setLayout(self.tab1.layout)

        # 텝1 전체 레이아웃 조립하기
        self.tab1En.layout.addWidget(self.tab1)
        self.tab1En.layout.addWidget(self.test)
        self.tab1En.setLayout(self.tab1En.layout)

        #시리얼 통신 정의하기 윈도우 및 리눅스 설정
        self.serial = QtSerialPort.QSerialPort('COM9', baudRate = QtSerialPort.QSerialPort.Baud115200, readyRead = self.receive)
        #self.serial = QtSerialPort.QSerialPort('/dev/ttyACM0', baudRate=QtSerialPort.QSerialPort.Baud115200, readyRead=self.receive)


        # 결과화면 돌리기
        return self.tab1En

    #시리얼 데이터 수신하는 함수
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            listext = list(text)

            a = 0
            temp = ''
            for i in listext:
                if i != 'n':
                    temp += i
                else:
                    a += 1
                    if a == 1:
                        self.textLivingroom.setText(temp.rstrip())
                    elif a == 2:
                        self.textRoom1.setText(temp.rstrip())
                    elif a == 3:
                        self.textRoom2.setText(temp.rstrip())
                    elif a == 4:
                        self.textBathroom.setText(temp.rstrip())
                    elif a == 5:
                        self.textToilet.setText(temp.rstrip())
                    elif a == 6:
                        self.textWater.setText(temp.rstrip())
                    elif a == 7:
                        self.textPIR.setText(temp.rstrip())
                    elif a == 8:
                        self.textGas.setText(temp.rstrip())
                    temp = ''

            self.test.setText("현재시간 : "+ text[len(text)-21:])

    #시리얼 통신 연결하는 함수
    def ConnectSerial(self):
        if not self.serial.isOpen():
            if not self.serial.open(QtCore.QIODevice.ReadWrite):
                print(1)
        else:
            self.serial.close()


    def GraphUI(self):
        #2번 탭 코드
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        # 2번 탭
        self.tab2 = QWidget()
        self.tab2.layout = QVBoxLayout(self)  # q위젯 형태의 탭 선언
        self.tab2Top = QWidget()
        self.tab2Top.layout = QHBoxLayout(self)

        #그래프 버튼
        self.Refresh = QPushButton('Refresh')
        self.Before = QPushButton('◀')
        self.Future = QPushButton('▶')

        # 버튼동작
        self.Refresh.clicked.connect(self.DrawGraph)
        self.Before.clicked.connect(self.DownChoiceday)
        self.Future.clicked.connect(self.UpChoiceday)
        self.choiceday = 0

        #Top레이아웃 조립하기
        self.tab2Top.layout.addWidget(self.Before)
        self.tab2Top.layout.addWidget(self.Refresh)
        self.tab2Top.layout.addWidget(self.Future)
        self.tab2Top.setLayout(self.tab2Top.layout)

        #전체 레이아웃 조립하기
        self.tab2.layout.addWidget(self.tab2Top)
        self.tab2.layout.addWidget(self.canvas)
        self.tab2.setLayout(self.tab2.layout)

        #결과화면 돌리기
        return self.tab2

    #날짜 변경하는 함수
    def UpChoiceday(self):
        self.choiceday += 1
        self.DrawGraph()

    # 날짜 변경하는 함수
    def DownChoiceday(self):
        self.choiceday -= 1
        self.DrawGraph()

    def DrawGraph(self):
        #2번 탭에 그래프 그리는 함수

        #오늘 날짜 설정하기
        self.TodayDates = (datetime.now() + timedelta(days = self.choiceday)).strftime('%Y-%m-%d')

        names = ['LivingRoom', 'Room1', 'Room2', 'Bathroom', 'Toilet', 'Water', 'PIR', 'Gas']

        # sql 연결설정하기, db 정보는 알아서 채우기!
        conn = pymysql.connect(host='', user='', password='', db='', charset='utf8')
        cursor = conn.cursor()

        # 전체 데이터 수집
        cursor.execute("SELECT *FROM test")
        test = cursor.fetchall()

        Today = []
        TodayString = []
        TodayTemp = []

        # 특정 날짜의 데이터 추출
        for i in test:
            if i[8].decode('utf8') == self.TodayDates:
                Today.append(i)

        # 데이터 변환
        for i in Today:
            for j in i:
                try:
                    TodayTemp.append(int(j))  # 날짜를 제외한 나머지 값은 정수 형태로 변환
                except:
                    TodayTemp.append(str(j.decode('utf8')))  # 날짜만 문자열로 변환
            TodayString.append(TodayTemp)
            TodayTemp = []

        # 시간대별로 정렬
        TodayString.sort(key=lambda x: x[9])

        x_value = list(range(24))
        y_value_LivingRoom = []
        y_value_Room1 = []
        y_value_Room2 = []
        y_value_Bathroom = []
        y_value_Toilet = []
        y_value_Water = []
        y_value_PIR = []
        y_value_Gas = []

        # 그래프 데이터 입력
        a = 0
        for i in TodayString:
            y_value_LivingRoom.append(i[0])
            y_value_Room1.append(i[1])
            y_value_Room2.append(i[2])
            y_value_Bathroom.append(i[3])
            y_value_Toilet.append(i[4])
            y_value_Water.append(i[5])
            y_value_PIR.append(i[6])
            y_value_Gas.append(i[7])
            a += 1

        # 특정한 시간대 데이터 없을 경우
        if a != 23:
            for i in range(a, 24):
                y_value_LivingRoom.append(0)
                y_value_Room1.append(0)
                y_value_Room2.append(0)
                y_value_Bathroom.append(0)
                y_value_Toilet.append(0)
                y_value_Water.append(0)
                y_value_PIR.append(0)
                y_value_Gas.append(0)

        #차트 그리기
        self.fig.clear()
        plot = self.fig.add_subplot(111)
        plot.plot(x_value, y_value_LivingRoom, label = names[0])
        plot.plot(x_value, y_value_Room1, label = names[1])
        plot.plot(x_value, y_value_Room2, label = names[2])
        plot.plot(x_value, y_value_Bathroom, label = names[3])
        plot.plot(x_value, y_value_Toilet, label = names[4])
        plot.plot(x_value, y_value_Water, label = names[5])
        plot.plot(x_value, y_value_PIR, label = names[6])
        plot.plot(x_value, y_value_Gas, label = names[7])

        plot.set_xlabel("Hour")
        plot.set_title(self.TodayDates)
        plot.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IOTMonitor()
    window.show()
    app.exec_()
