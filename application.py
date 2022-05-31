import time
from layouts.layout import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Aplicacao(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.maOutput.setReadOnly(1)
        self.vcOutput.setReadOnly(1)
        self.vac0Output.setReadOnly(1)
        self.vac1Output.setReadOnly(1)
        self.vbc0Output.setReadOnly(1)
        self.vbc1Output.setReadOnly(1)
        self.mac0Output.setReadOnly(1)
        self.mac1Output.setReadOnly(1)
        self.mbc0Output.setReadOnly(1)
        self.mbc1Output.setReadOnly(1)
        self.btnCalcular.clicked.connect(self.calcular)

    def calcular(self):

        self.statusBar().setStyleSheet("background-color :")
        self.statusBar().showMessage("")
        va, vb, x1, x2 = self.recebe_valores()
        vc, ma = self.reacoes_de_apoio(va, vb, x1, x2)
        vac0, vac1, vbc0, vbc1 = self.forca_cortante(va, vb, x1, x2)
        mac0, mac1, mbc0, mbc1 = self.momento_fletor(va, vb, x1, x2)
        self.maOutput.setText(str(ma))
        self.vcOutput.setText(str(vc))
        self.vac0Output.setText(str(vac0))
        self.vac1Output.setText(str(vac1))
        self.vbc0Output.setText(str(vbc0))
        self.vbc1Output.setText(str(vbc1))
        self.mac0Output.setText(str(mac0))
        self.mac1Output.setText(str(mac1))
        self.mbc0Output.setText(str(mbc0))
        self.mbc1Output.setText(str(mbc1))


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


    def forca_cortante(self, va, vb, x1, x2):
        vac0 = va - 0  # para x = 0
        vac1 = va - x1  # para x = x1
        vbc0 = vb - 0  # para x = 0
        vbc1 = vb - x2  # para x = 1

        return vac0, vac1, vbc0, vbc1

    def reacoes_de_apoio(self, va, vb, x1, x2):
        vc = va + vb
        ma = (vc * x1) - (vb * (x2 + x1))

        return vc, ma

    def momento_fletor(self, va, vb, x1, x2):
        mac0 = va - 0
        mac1 = va - ((x1 ** 2) / 2)
        mbc0 = vb - 0
        mbc1 = vb - ((x2 ** 2) / 2)

        return mac0, mac1, mbc0, mbc1
