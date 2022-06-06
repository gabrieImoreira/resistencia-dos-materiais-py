from layouts.layout import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Aplicacao(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, x1=None, x2=None, vca0=None, vca1=None, vcb0=None, vcb1=None):
        super().__init__(parent)
        super().setupUi(self)
        self.x1 = x1
        self.x2 = x2
        self.vca0 = vca0
        self.vca1 = vca1
        self.vcb0 = vcb0
        self.vcb1 = vcb1
        self.vcOutput.setReadOnly(1)
        self.vca0Output.setReadOnly(1)
        self.vca1Output.setReadOnly(1)
        self.vcb0Output.setReadOnly(1)
        self.vcb1Output.setReadOnly(1)
        self.mca0Output.setReadOnly(1)
        self.mca1Output.setReadOnly(1)
        self.mcb0Output.setReadOnly(1)
        self.mcb1Output.setReadOnly(1)

        self.graficoFc = CanvasGrafico()
        self.fcGrafico.addWidget(self.graficoFc)
        self.graficoMf = CanvasGrafico()
        self.mfGrafico.addWidget(self.graficoMf)

        self.btnCalcular.clicked.connect(self.calcular)
        self.btnGerarGrafico.clicked.connect(self.update_graph)

    def update_graph(self):
        print(self.vca0);
        if self.vca1 == 0 or self.vca1 is None:
            self.statusBar().setStyleSheet("background-color : red")
            self.statusBar().showMessage("Insira valores válidos para gerar o gŕafico.")
        else:
            CanvasGrafico.update_graph(self.graficoFc, self.x1, self.x2, self.vca0, self.vca1, self.vcb0, self.vcb1)
            CanvasGrafico.update_graph(self.graficoMf, self.x1, self.x2, self.mca0, self.mca1, self.mcb0, self.mcb1)

    def calcular(self):

        self.statusBar().setStyleSheet("background-color :")
        self.statusBar().showMessage("")
        va, vb, self.x1, self.x2 = self.recebe_valores()
        vc = self.reacoes_de_apoio(va, vb, self.x1, self.x2)
        self.vca0, self.vca1, self.vcb0, self.vcb1 = self.forca_cortante(va, vb, vc, self.x1, self.x2)
        self.mca0, self.mca1, self.mcb0, self.mcb1 = self.momento_fletor(va, vb, self.x1, self.x2)
        self.vcOutput.setText(str(vc))
        self.vca0Output.setText(str(self.vca0))
        self.vca1Output.setText(str(self.vca1))
        self.vcb0Output.setText(str(self.vcb0))
        self.vcb1Output.setText(str(self.vcb1))
        self.mca0Output.setText(str(self.mca0))
        self.mca1Output.setText(str(self.mca1))
        self.mcb0Output.setText(str(self.mcb0))
        self.mcb1Output.setText(str(self.mcb1))

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

class CanvasGrafico(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        self.draw()

    def update_graph(self, x1, x2, vca0, vca1, vcb0, vcb1):
        X = [0, x1, x1, x1 + x2]
        Y = [vca0, vca1, vcb0, vcb1]
        self.ax.clear()
        self.ax.plot(X, Y)
        self.draw()

