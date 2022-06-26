from PyQt5 import QtWidgets
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        temperature = [30, 40, 34, 32, 33, 31, 42, 32, 35, 45, 41]
        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(["Algoritmos graficos"])
    main = MainWindow()
    main.show()
    app.exec_()


if __name__ == "__main__":
    main()
