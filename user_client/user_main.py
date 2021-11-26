import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import user_chart
import user_prediction


form_class = uic.loadUiType("test.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fig = plt.Figure()
        self.initUI()
        self.pushButton.clicked.connect(self.push_function)

    def initUI(self):
        combo = self.comboBox.currentText()
        combo = combo.split(' ')
        code = combo[0]
        company = combo[1]
        RNN = user_prediction.load_predict(code, company)
        self.prediction_1.append(RNN)
        # self.prediction_2.append(prediction_2)

        self.canvas = FigureCanvas(self.fig)

        self.chart.addWidget(self.canvas)
        user_chart.draw_chart(self, code, company)
        self.canvas.draw()
    def push_function(self):
        self.prediction_1.clear()
        self.prediction_2.clear()
        self.fig.clear()


        combo = self.comboBox.currentText()
        combo = combo.split(' ')
        code = combo[0]
        company = combo[1]
        RNN = user_prediction.load_predict(code, company)
        self.prediction_1.append(RNN)
        #self.prediction_2.append(prediction_2)

        self.canvas = FigureCanvas(self.fig)

        self.chart.addWidget(self.canvas)
        user_chart.draw_chart(self, code, company)
        self.canvas.draw()

if __name__== "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()