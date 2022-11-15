from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pylab import rcParams
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.loaded_model = None
        self.data = None
        self.result = None
        self.mainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 160, 971, 600))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.imglabel = QLabel(self.verticalLayoutWidget_2)
        pixmap = QPixmap('test.png')

        # self.imglabel.setPixmap(pixmap)
        # self.label_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        # self.label_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.imglabel)
        # vbox.addWidget(self.label_size)
        self.verticalLayout_2.addLayout(vbox)

        # canvas = FigureCanvas(Figure(figsize=(4, 3)))
        # vbox = QVBoxLayout()
        # vbox.addWidget(canvas)
        #
        #
        # self.ax = canvas.figure.subplots()
        # self.ax.plot([0, 1, 2], [1, 5, 3], '-')
        #
        # self.verticalLayout_2.addLayout(vbox)



        # self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setGeometry(QtCore.QRect(20, 60, 681, 87))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 85))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        # self.tableView.setGeometry(QtCore.QRect(10, 10, 651, 71))
        # self.tableView.setObjectName("tableView")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tableWidget = QTableWidget(self.centralwidget)

        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 681, 127))
        self.tableWidget.setRowCount(672)
        self.tableWidget.setColumnCount(7)
        self.set_table()


        # 버튼
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 70, 93, 28))
        self.pushButton.setText("데이터 로드")
        self.pushButton.setObjectName("데이터 로드")
        self.pushButton.clicked.connect(self.load_csv)

        self.pushButton_2 = QtWidgets.QPushButton('예측', self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 110, 93, 28))
        self.pushButton_2.setObjectName("예측")
        self.pushButton_2.clicked.connect(self.predict)


        # 출력 레이블
        # self.label = QLabel('최대전력', self.centralwidget)
        # self.label.setText('최대전력')
        # self.label.setGeometry(QtCore.QRect(840, 80, 64, 15))
        # self.label.setObjectName("label")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(840, 110, 64, 15))
        # self.label_2.setObjectName("label_2"),
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(930, 80, 64, 15))
        # self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(930, 110, 64, 15))
        # self.label_4.setObjectName("label_4")

        self.label1 = QLabel('최대전력', self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(840, 60, 64, 15))
        self.label2 = QLabel(None, self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(840, 100, 64, 15))
        self.label3 = QLabel('발생지점', self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(960, 60, 64, 15))
        self.label4 = QLabel(None, self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(960, 100, 64, 15))
        self.label1.resize(300, 40)
        self.label2.resize(300, 40)
        self.label3.resize(300, 40)
        self.label4.resize(300, 40)


        MainWindow.setCentralWidget(self.centralwidget)


        # 메뉴바

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.setNativeMenuBar(False)
        filemenu = self.menubar.addMenu('File')

        load_model_action = QAction('Load model', self.menubar )
        load_model_action.setShortcut('Ctrl+L')
        load_model_action.triggered.connect(self.load_model)

        exit_action = QAction('Exit', self.menubar )
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        data_load_action = QAction('Data load', self.menubar )
        data_load_action.triggered.connect(self.load_csv)

        filemenu.addAction(load_model_action)
        filemenu.addAction(data_load_action)
        filemenu.addAction(exit_action)


        # 상태바

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))
        # self.label_3.setText(_translate("MainWindow", "TextLabel"))
        # self.label_4.setText(_translate("MainWindow", "TextLabel"))

    def set_table(self):
        self.tableWidget.setHorizontalHeaderLabels(['생산량', '기온', '풍속', '습도', '강수량', '요일', '전력'])
        if self.data is not None:
            for i in range(672):
                for j in range(7):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.data.iloc[i, j])))
        else:
            for i in range(672):
                for j in range(7):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(None)))


    def load_model(self):
        fname, _ = QFileDialog.getOpenFileName(self.mainWindow, 'Load Model', '')

        if fname:
            self.loaded_model = tf.keras.models.load_model(fname)
            self.statusbar.showMessage('Model loaded.')

    def load_csv(self):
        fname, _ = QFileDialog.getOpenFileName(self.mainWindow, 'Open File', '')

        if fname:
            self.data = pd.read_csv(fname)
            self.statusbar.showMessage('CSV File loaded.')

        self.set_table()

    def new_pix(self):
        pixmap = QPixmap('test.png')

        self.imglabel.setPixmap(pixmap)


    def predict(self):

        if self.loaded_model is not None and  self.data is not None:
            inputs = np.array([self.data.values])
            self.label4.setText('start')
            self.result = self.loaded_model.predict(inputs)[0]

            max_time = 15 + np.argmax(self.result) * 15
            max_time_str = f'{max_time//60} 시 {max_time % 60} 분'
            max_value = np.max(self.result)

            self.label2.setText(str(max_value)[:6]+'kW')
            self.label4.setText(max_time_str)

            plt.figure(figsize=(10, 5))

            plt.plot(np.arange(1, 97), self.result.reshape(-1, ), linewidth=3, color='red',
                     label='peak_EP')
            plt.legend()
            plt.xticks(np.arange(0, 97, 4), np.arange(0, 25))
            plt.xlabel('hour', fontsize=24)
            plt.ylabel('peak_EP', fontsize=24)
            plt.grid()

            plt.savefig('test.png')

            self.new_pix()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

