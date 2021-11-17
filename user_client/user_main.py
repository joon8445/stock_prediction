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


        self.prediction_1.append(prediction_1)
        self.prediction_2.append(prediction_2)

        self.canvas = FigureCanvas(self.fig)

        self.chart.addWidget(self.canvas)
        x = np.arange(0, 100, 1)
        y = np.sin(x)

        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("stock graph")
        ax.legend()
        self.canvas.draw()

if __name__== "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()