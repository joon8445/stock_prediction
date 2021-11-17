import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pandas_datareader import data as pdr
import yfinance as yf

form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fig = plt.Figure()

        real_price = 110000

        predict_price_1 = 113000
        prediction_1 = '2021. 11. 03. Data 기준 11.4일 예측가 : '+str(predict_price_1)+'\n전일 거래 예측 종가 오차율 : '
        prediction_1 += "{:.2f}".format((1 - real_price / predict_price_1)*100)
        predict_price_2 = 114000
        prediction_2 = '2021. 11. 03. Data 기준 11.4일 예측가 : ' + str(predict_price_1) + '\n전일 거래 예측 종가 오차율 : '
        prediction_2 += "{:.2f}".format((1 - real_price / predict_price_2) * 100)
        self.prediction_1.append(prediction_1)
        self.prediction_2.append(prediction_2)

        self.canvas = FigureCanvas(self.fig)

        self.chart.addWidget(self.canvas)
        yf.pdr_override()
        print('override')
        sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')  # kospi = XXXXXX.KS
        msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')  # kosdaq = symbol
        print('get_data')
        tmp_msft = msft.drop(columns='Volume')
        tmp_msft.tail()


        # plot(x, y, 마커 형태,[,label='Label'])
        ax = self.fig.add_subplot(111)
        ax.plot(sec.index, sec.Close, 'b', label='SSEC')  # x = dateindex, y = Close,
        ax.legend(loc='best')

if __name__== "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()