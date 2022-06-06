from layouts.layout import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Aplicacao(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.vcOutput.setReadOnly(1)
        self.vca0Output.setReadOnly(1)
        self.vca1Output.setReadOnly(1)
        self.vcb0Output.setReadOnly(1)
        self.vcb1Output.setReadOnly(1)
        self.mca0Output.setReadOnly(1)
        self.mca1Output.setReadOnly(1)
        self.mcb0Output.setReadOnly(1)
        self.mcb1Output.setReadOnly(1)

        self.grafico = Canvas_grafico()
        self.fcGrafico.addWidget(self.grafico)

        self.btnCalcular.clicked.connect(self.calcular)
        self.btnGerarGrafico.clicked.connect(self.update_graph)

    def update_graph(self, x1, x2, vca0, vca1, vcb0, vcb1):
        X = [0, x1, x1, x1 + x2]
        Y = [vca0, vca1, vcb0, vcb1]
        self.plt.title("Força cortante")
        self.plt.xlabel("Tamanho em metros")
        self.plt.plot(X, Y)
        self.plt.show()

    def calcular(self):

        self.statusBar().setStyleSheet("background-color :")
        self.statusBar().showMessage("")
        va, vb, x1, x2 = self.recebe_valores()
        vc = self.reacoes_de_apoio(va, vb, x1, x2)
        vca0, vca1, vcb0, vcb1 = self.forca_cortante(va, vb, vc, x1, x2)
        mca0, mca1, mcb0, mcb1 = self.momento_fletor(va, vb, x1, x2)
        self.vcOutput.setText(str(vc))
        self.vca0Output.setText(str(vca0))
        self.vca1Output.setText(str(vca1))
        self.vcb0Output.setText(str(vcb0))
        self.vcb1Output.setText(str(vcb1))
        self.mca0Output.setText(str(mca0))
        self.mca1Output.setText(str(mca1))
        self.mcb0Output.setText(str(mcb0))
        self.mcb1Output.setText(str(mcb1))


    def recebe_valores(self):
        try:
            va = float(self.vaInput.text())
            vb = float(self.vbInput.text())
            x1 = float(self.x1Input.text())
            x2 = float(self.x2Input.text())

            return va, vb, x1, x2
        except:
            self.statusBar().setStyleSheet("background-color : red")
            self.statusBar().showMessage("Digite apenas números inteiros ou números no formato americano.")
            return False, False, False, False


    def forca_cortante(self, va, vb, vc, x1, x2):
        vca0 = (vc - va) * 0  # para x = 0
        vca1 = (vc - va) * x1  # para x = x1
        vcb0 = (vc - vb) * 0  # para x = 0
        vcb1 = (vc - vb) * x2  # para x = 1

        return vca0, vca1, vcb0, vcb1

    def reacoes_de_apoio(self, va, vb, x1, x2):
        vc = va + vb
        #ma = (vc * x1) - (vb * (x2 + x1))

        return vc

    def momento_fletor(self, va, vb, x1, x2):
        mca0 = va * 0
        mca1 = - va * x1
        mcb0 = vb * 0
        mcb1 = - vb * x2

        return mca0, mca1, mcb0, mcb1

class Canvas_grafico(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        vca0 = 500
        vca1 = 475
        vcb0 = 200
        vcb1 = 195
        X = [0, 8, 8, 10]
        Y = [vca0, vca1, vcb0, vcb1]
        self.ax.plot(X, Y)
        self.draw()